# tee ratkaisu tänne
def hae_nimi(tiedosto: str, sana: str):
    tulos = []
    loydetyt = []
    ruuat = []
    with open(tiedosto) as txt:
        
        for resepti in txt:
            sanat = resepti.strip()
            if sanat == "":
                loydetyt.append(ruuat)
                ruuat = []
            else:
                ruuat.append(sanat)

    loydetyt.append(ruuat)            
   
    print(loydetyt)
    for x in loydetyt:
        
        if sana.lower() in x[0].lower():
            tulos.append(x[0])
            
        
    
    return tulos

def hae_aika(tiedosto: str, aika: int):
    loydetyt = []
    nimi = ""
    with open(tiedosto) as txt:
        
        for resepti in txt:
            resepti = resepti.replace("\n", "")
            if resepti.isnumeric() and int(resepti) <= aika :
                loydetyt.append(f"{nimi}, valmistusaika {resepti} min")
        
            else:
                nimi = resepti
    return loydetyt

def hae_raakaaine(tiedosto: str, aine: str):
    loydetyt = []
    resepti = []
    with open(tiedosto) as txt:
        
        for x in txt:
            x = x.strip()
            
            if x == '':
                resepti = []

            if x != "":
                resepti.append(x)

            if aine in x:
                loydetyt.append(f"{resepti[0]}, valmistusaika {resepti[1]} min")
    
    return loydetyt


if __name__ == "__main__":


    loydetyt = hae_nimi("reseptit1.txt", "pulla")

    for resepti in loydetyt:
        print(resepti)