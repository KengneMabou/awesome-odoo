import requests
import re

README_FILE = "README.md"

def extract_links(text):
    """Extrae todos los enlaces del archivo README.md"""
    return re.findall(r'\[.*?\]\((http[s]?://.*?)\)', text)

def check_link(url):
    """Verifica si el enlace es accesible"""
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code < 400
    except requests.RequestException:
        return False

def main():
    with open(README_FILE, "r", encoding="utf-8") as file:
        content = file.read()
    
    links = extract_links(content)
    
    if not links:
        print("No se encontraron enlaces en el archivo README.md.")
        return
    
    print(f"🔎 Verificando {len(links)} enlaces...\n")
    
    broken_links = []
    for link in links:
        if not check_link(link):
            print(f"❌ Roto: {link}")
            broken_links.append(link)
        else:
            print(f"✅ Válido: {link}")

    if broken_links:
        print("\n⚠️ Enlaces rotos encontrados:")
        for link in broken_links:
            print(f"- {link}")
    else:
        print("\n✅ No se encontraron enlaces rotos.")

if __name__ == "__main__":
    main()
