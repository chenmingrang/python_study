#循环导入，应从设计上避免此种情况
from study_further.python_core.module_import_export.cycle_imp_b import b

def a():
    print("====a======")
    b()

a()