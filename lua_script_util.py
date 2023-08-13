import subprocess
import os
import requests
from bs4 import BeautifulSoup

print("LIB: Lua Script Util. Version: 10.12.31")

def run_lua_script(lua_cmd, *args):
    result = subprocess.run(lua_cmd + list(args), capture_output=True, text=True, input=None if not args else '\n'.join(args))
    if result.returncode == 0:
        output = result.stdout.strip()
        print(output)
        return output
    else:
        error_message = result.stderr.strip() if result.stderr else "An error occurred while executing the Lua script."
        raise RuntimeError(error_message)

def search_luarocks(query):
    url = f"https://luarocks.org/search?q={query}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        modules = soup.find_all("div", class_="module")

        if modules:
            module = modules[0]
            module_name = module.find("h2").text.strip()
            module_desc = module.find("p", class_="module-description").text.strip()

            print(f"Module: {module_name}")
            print(f"Description: {module_desc}")

            module_url = module.find("a", class_="module-link")["href"]
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
    result = subprocess.run(lua_cmd, capture_output=True, text=True)
    if result.returncode == 0:
        output = result.stdout.strip()
        return output
    else:
        error_message = result.stderr.strip() if result.stderr else "An error occurred while getting Lua version."
        raise RuntimeError(error_message)

lua_version = get_lua_version()
print(lua_version)
    
def luacreate(script_name):
    script_path = f"{script_name}.lua"
    if os.path.exists(script_path):
        confirm = input(f"File {script_path} already exists. Do you want to overwrite it? (y/n): ")
        if confirm.lower() != "y":
            return
    with open(script_path, "w") as f:
        f.write("-- Your Lua script here")
    print(f"Created file: {script_path}")

def luarun(script_path, *args):
    lua_cmd = ['Lua/lua.exe', script_path]
    return run_lua_script(lua_cmd, *args)

def luascriptcompilation(script_path, output_path):
    output_path = os.path.splitext(output_path)[0] + ".out"  # Add ".out" extension
    lua_cmd = ['Lua/luac.exe', '-o', output_path, script_path]
    return run_lua_script(lua_cmd)

def wluarun(script_path, *args):
    lua_cmd = ['Lua/wlua.exe', script_path]
    return run_lua_script(lua_cmd, *args)
