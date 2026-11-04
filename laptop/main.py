import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("laptop_data.csv")

df.drop(["Unnamed: 0", "Company"], axis=1, inplace=True)

df["Ram"] = df["Ram"].str.replace("GB", "").astype(int)#заміняємо на число. Наприклад: 12 ГБ ---> 12
df['Weight'] = df["Weight"].str.replace("kg", "").astype(float)

resolution = df["ScreenResolution"].str.split().str[-1]#Розділяємо речення за пробілами і бере останнє значення. Наприклад: Я граю в кс2---->кс2
df["Res_X"] = resolution.str.split("x").str[0].astype(int)#Розділяємо два числа які залишились з попереднього коду і створюємо два нових стовпця. Наприклад: 2560x1600 ----> 2560 | 1600
df["Res_X"] = resolution.str.split("x").str[1].astype(int)
df.drop("ScreenResolution", axis=1, inplace=True)

ghz = df["Cpu"].str.split().str[-1]
df["Cpu_GHz"] = ghz.str.replace("GHz", "").astype(float)
df.drop("Cpu", axis=1, inplace=True)

df["Gpu_Brand"] = df["Gpu"].str.split().str[0]
df.drop("Gpu", axis=1, inplace=True)




def parse_memory(text):
    primary = text.split("+")[0].strip()
    size = primary.split()[0]
    if "TB" in size:
        return int(float(size.replace("TB", "").strip()) * 1024)
    elif "GB" in size:
        return int(float(size.replace("GB", "").strip()))
    else:
        return 0

def check_ssd(text):
    if "SSD" in text:
        return 1
    else:
        return 0

df["Memory_GB"] = df["Memory"].apply(parse_memory)
df["Is_SSD"] = df["Memory"].apply(check_ssd)
df.drop("Memory", axis=1, inplace=True)

df = pd.get_dummies(df, columns=["TypeName", "OpSys", "Gpu_Brand"], drop_first=True)#Gpu_Brand на NVidia|AMD|Cpu_Grafics
#                                                                                                   0     1     0
#                                                                                                   0     0     1





x = df.drop("Price", axis=1)
y = df["Price"]
model = LinearRegression()
model.fit(x,y)

sample_laptop = pd.DataFrame([{
    "Inches": 13,
    "Ram": 128,
    "Weight": 2,
    "Res_X": 7680,
    "Res_Y": 4320,
    "Cpu_GHz": 4.3,
    "Memory_GB": 2048,
    "Is_SSD": 1,
    "TypeName_Gaming": 0,
    "TypeName_Netbook": 0,
    "TypeName_Notebook": 1,
    "TypeName_Ultrabook": 0,
    "TypeName_Workstation": 0,
    "OpSys_Chrome OS": 0,
    "OpSys_Linux": 0,
    "OpSys_Mac OS X": 1,
    "OpSys_No OS": 0,
    "OpSys_Windows 10": 0,
    "OpSys_Windows 10 S": 0,
    "OpSys_Windows 7": 0,
    "OpSys_macOS": 0,
    "Gpu_Brand_Intel": 0,
    "Gpu_Brand_Nvidia": 1
}]).reindex(columns=x.columns, fill_value=0)

predicted_price = model.predict(sample_laptop)[0]
print(predicted_price*0.47)