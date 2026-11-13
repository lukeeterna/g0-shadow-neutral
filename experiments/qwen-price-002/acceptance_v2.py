"""Frozen v2 independent Judge (ValueError AST constructor allowed) for local Qwen → GitHub isolated pipeline."""
import ast
import hashlib
import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent
CODE = ROOT / "price_eur.py"

def _static_gate():
    if not CODE.is_file():
        raise RuntimeError("STOP_WORKER_CODE_MISSING")
    raw = CODE.read_bytes()
    if len(raw) > 10000:
        raise RuntimeError("STOP_WORKER_SOURCE_OVERSIZE")
    tree = ast.parse(raw, filename="price_eur.py")
    body = [n for n in tree.body if not isinstance(n, ast.Expr) or not isinstance(n.value, ast.Constant) or not isinstance(n.value.value, str)]
    if len(body) != 1 or not isinstance(body[0], ast.FunctionDef):
        raise RuntimeError("STOP_NOT_EXACTLY_ONE_FUNCTION")
    fn = body[0]
    if fn.name != "format_eur" or len(fn.args.args) != 1 or fn.args.args[0].arg != "cents" or fn.decorator_list:
        raise RuntimeError("STOP_WORKER_FUNCTION_CONTRACT")
    forbidden = (ast.Import,ast.ImportFrom,ast.ClassDef,ast.AsyncFunctionDef,ast.Lambda,ast.Global,ast.Nonlocal,ast.With,ast.AsyncWith,ast.Try,ast.Yield,ast.YieldFrom,ast.Await,ast.Delete,ast.FunctionDef)
    allowed_calls = {"str","int","divmod","isinstance","type","format","ValueError"}
    for n in ast.walk(fn):
        if n is not fn and isinstance(n, forbidden):
            raise RuntimeError("STOP_FORBIDDEN_AST_NODE_"+type(n).__name__)
        if isinstance(n, ast.Name) and n.id.startswith("__"):
            raise RuntimeError("STOP_FORBIDDEN_DUNDER")
        if isinstance(n, ast.Attribute) and n.attr not in {"replace","zfill"}:
            raise RuntimeError("STOP_FORBIDDEN_ATTRIBUTE")
        if isinstance(n, ast.Call):
            f=n.func
            if isinstance(f,ast.Name) and f.id in allowed_calls:
                continue
            if isinstance(f,ast.Attribute) and f.attr in {"replace","zfill"}:
                continue
            raise RuntimeError("STOP_FORBIDDEN_FUNCTION_CALL")
    return hashlib.sha256(raw).hexdigest()

class FrozenPriceJudge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.code_sha256 = _static_gate()
        module_spec = importlib.util.spec_from_file_location("price_eur",CODE)
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        cls.fn = staticmethod(module.format_eur)

    def test_01_zero(self): self.assertEqual(self.fn(0),"€0,00")
    def test_02_one_cent(self): self.assertEqual(self.fn(1),"€0,01")
    def test_03_ninety_nine(self): self.assertEqual(self.fn(99),"€0,99")
    def test_04_one_euro(self): self.assertEqual(self.fn(100),"€1,00")
    def test_05_one_euro_five(self): self.assertEqual(self.fn(105),"€1,05")
    def test_06_nine_ninety_nine(self): self.assertEqual(self.fn(999),"€9,99")
    def test_07_twelve_euro(self): self.assertEqual(self.fn(1234),"€12,34")
    def test_08_thousands(self): self.assertEqual(self.fn(123456),"€1.234,56")
    def test_09_hundred_thousands(self): self.assertEqual(self.fn(99999999),"€999.999,99")
    def test_10_maximum(self): self.assertEqual(self.fn(999999999),"€9.999.999,99")
    def test_11_negative(self):
        with self.assertRaises(ValueError): self.fn(-1)
    def test_12_over_maximum(self):
        with self.assertRaises(ValueError): self.fn(1000000000)
    def test_13_boolean(self):
        with self.assertRaises(ValueError): self.fn(True)
    def test_14_float(self):
        with self.assertRaises(ValueError): self.fn(1.0)
    def test_15_string(self):
        with self.assertRaises(ValueError): self.fn("100")
    def test_16_none(self):
        with self.assertRaises(ValueError): self.fn(None)

if __name__=="__main__":
    unittest.main(verbosity=2)
