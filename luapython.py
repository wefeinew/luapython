import subprocess
import os
import requests
import lupa
from bs4 import BeautifulSoup

print("LIB: Lua Python. By Pythonlua.org")

def run_lua_script(lua_cmd, *args):
    result = subprocess.run(lua_cmd + list(args), capture_output=True, text=True, input=None if not args else '\n'.join(args))
    if result.returncode == 0:
        output = result.stdout.strip()
        print(output)
        return output
    else:
        error_message = result.stderr.strip() if result.stderr else "An error occurred while executing the Lua script."
        raise RuntimeError(error_message)

def execute_lua_code(code):
    lua = lupa.LuaRuntime()
    lua.execute(code)

def search_luarocks(query):
    url = f"https://luarocks.org/search?q={query}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        modules = soup.find_all("a", class_="module-link")

        if modules:
            module = modules[0]
            module_name = module.text.strip()
            module_url = module["href"]

            download_url = f"https://luarocks.org{module_url}/download"
            module_response = requests.get(download_url)

            if module_response.status_code == 200:
                with open(f"{module_name}.rock", "wb") as file:
                    file.write(module_response.content)
                print(f"Module '{module_name}' successfully downloaded")
            else:
                print("An error occurred while downloading the module")
        else:
            print("Modules not found")
    else:
        print("An error occurred while executing the request")

def lua_terminal():
    lua_cmd = ['Lua/lua.exe']
    process = subprocess.Popen(lua_cmd)

def get_lua_version():
    lua_cmd = ['Lua/lua.exe', '-v']
    process = subprocess.Popen(lua_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
    output, error = process.communicate() 
    
    if process.returncode != 0:
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
        f.write("")
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
