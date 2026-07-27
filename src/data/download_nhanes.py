import requests
import os


FILES = {

    "demographics":
    "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.XPT",

    "body":
    "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.XPT",

}


OUTPUT = "data/raw/nhanes"


os.makedirs(
    OUTPUT,
    exist_ok=True
)


for name, url in FILES.items():

    print(f"Downloading {name}")

    response = requests.get(url)

    with open(
        f"{OUTPUT}/{name}.XPT",
        "wb"
    ) as f:

        f.write(response.content)


print("Download complete")