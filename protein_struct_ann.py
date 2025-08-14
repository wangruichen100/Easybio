from pymol import cmd

def highlight_residues_with_cartoon_and_surface(cif_file, txt_file):
    # 加载 CIF 文件
    cmd.load(cif_file)
    
    # 显示蛋白质的 Cartoon 和 Surface
    cmd.show("cartoon")
    cmd.show("surface")
    cmd.set("transparency", 0.8)  # 设置表面透明度为50%
    
    # 显示所有的蛋白质结构为灰色
    cmd.color("0x8ECFC9")

    # 读取 TXT 文件
    with open(txt_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # 提取目标位点的列表
    target_residues = set()
    for line in lines[1:]:  # 跳过标题行
        line = line.strip()
        if not line:
            continue
        residue, _ = line.split()  # 假设文件格式为 "site group"
        target_residues.add(residue)
    
    # 遍历所有残基，将目标位点标记为红色并显示标签
    for residue in target_residues:
        selection_name = f"resi_{residue}"
        cmd.select(selection_name, f"resi {residue}")
        cmd.color("red", selection_name)


    # 清理选择
    cmd.deselect()
    
    # 优化视图
    cmd.bg_color("white")
    cmd.set("ray_opaque_background", 0)

# 替换为您的文件路径
cif_file = r"xxxxxx\fold_e_model_0.cif"  # CIF 文件路径
txt_file = r"xxxxx\ann_info.txt"  # TXT 文件路径

# 执行函数
highlight_residues_with_cartoon_and_surface(cif_file, txt_file)
