import subprocess
import os

print("LIB: Lua Python. By Pythonlua.org")

def run_lua_script(lua_cmd, *args):
    result = subprocess.run(lua_cmd + list(args), capture_output=True, text=True, input=None if not args else '\n'.join(args))
    if result.returncode == 0:
        output = result.stdout.strip()
        print(output)  # Вывод результата в консоль
        return output
    else:
        error_message = result.stderr.strip() if result.stderr else "An error occurred while executing the Lua script."
        raise RuntimeError(error_message)

def lua_terminal():
    lua_cmd = ['Lua/lua.exe']
    process = subprocess.Popen(lua_cmd)

def get_lua_version():
    lua_cmd = ['Lua/lua.exe', '-vef']
    process = subprocess.Popen(lua_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
    output, error = process.communicate()  # Дождаться завершения процесса и получить вывод
    
    if process.returncode != 0:  # Проверить код возврата процесса на наличие ошибок
        error_message = error.strip() if error else "An error occurred while executing the Lua"
        raise RuntimeError(error_message)
    
    return output.strip()

lua_version = get_lua_version()
print(lua_version)
    
def luacreate(script_name):
    script_path = f"{script_name}.lua"
    if os.path.exists(script_path):
        confirm = input(f"File {script_path} already exists. Do you want to overwrite it? (y/n): ")
        if confirm.lower() != "y":
            return
    with open(script_path, "w") as f:
        f.write("")  # Empty file
    print(f"Created file: {script_path}")

def luarun(script_path, *args):
    lua_cmd = ['Lua/lua.exe', script_path]
    return run_lua_script(lua_cmd, *args)

def luascriptcompilation(script_path, output_path):
    lua_cmd = ['Lua/luac.exe', '-o', output_path, script_path]
    return run_lua_script(lua_cmd)

def wluarun(script_path, *args):
    lua_cmd = ['Lua/wlua.exe', script_path]
    return run_lua_script(lua_cmd, *args)
