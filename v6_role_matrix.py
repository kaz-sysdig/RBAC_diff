import json

# ファイルからJSONデータを読み込む
with open('v6_rbac.json', 'r') as f:
    python_dict = json.load(f)

# Initialize matrix with headers
matrix = [
    ["Role Group", "Role Name", "Name", "Permission", "Description", "Action", 
     "Item Display Name", "Item Description", "Category Name", "Category Description"]
]

# 'roles' 下の各階層（例えば 'SERVICE', 'ADDITIONAL' など）をイテレート
for role_group, role_group_content in python_dict.get("roles", {}).items():
    # 各階層内のロール（例えば 'ADMISSION_CONTROLLER_API_APP' など）をイテレート
    for role_name, roles in role_group_content.items():
        # 各ロール内の情報をイテレート
        for role in roles:
            row = [
                role_group,  # Role Group (e.g., 'SERVICE', 'ADDITIONAL')
                role_name,  # Role Name (e.g., 'ADMISSION_CONTROLLER_API_APP')
                role.get("name", ""), 
                role.get("permission", ""), 
                role.get("description", ""), 
                role.get("action", ""),
                role.get("itemDisplayName", ""),
                role.get("itemDescription", ""),
                role.get("categoryName", ""),
                role.get("categoryDescription", "")
            ]
            matrix.append(row)

# 2次元配列（マトリックス）を出力
for row in matrix:
    print("\t".join(row))

