import json
import sys
import os

# 检查命令行参数是否正确
if len(sys.argv) != 2:
    print("请提供以 .json 结尾的配置文件的路径作为命令行参数")
    sys.exit(1)

# 获取命令行参数中的配置文件路径
config_path = sys.argv[1]

# 检查配置文件是否存在
if not os.path.isfile(config_path):
    print("配置文件不存在")
    sys.exit(1)

# 检查配置文件的扩展名是否为 .json
if not config_path.endswith(".json"):
    print("请提供以 .json 结尾的配置文件的路径")
    sys.exit(1)

# 读取配置文件
with open(config_path, encoding='utf-8') as config_file:
    config = json.load(config_file)

# 递归将所有值设置为空字符串
def remove_values(data):
    if isinstance(data, dict):
        return {key: remove_values(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [remove_values(item) for item in data]
    else:
        return ""

# 将配置文件中的值设置为空字符串
new_config = remove_values(config)

# 构造新的文件名
dirname, basename = os.path.split(config_path)
filename, ext = os.path.splitext(basename)
new_filename = os.path.join(dirname, f"{filename}_rmvalue{ext}")

# 将更新后的配置写入新的 JSON 文件
with open(new_filename, "w", encoding='utf-8') as new_config_file:
    json.dump(new_config, new_config_file, indent=4, ensure_ascii=False)

print(f"已生成新的 JSON 文件：{new_filename}")
