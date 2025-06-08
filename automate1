{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "936cde4b-4c79-40cd-b2bb-3c1478db5fea",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "from selenium.webdriver.chrome.service import Service\n",
    "from selenium.webdriver.chrome.options import Options\n",
    "import pandas as pd\n",
    "import os\n",
    "from datetime import datetime\n",
    "import sys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f5c7477f-86a0-46ee-95dd-273402c9c801",
   "metadata": {},
   "outputs": [],
   "source": [
    "app_path=os.path.dirname(sys.executable)\n",
    "now=datetime.now()\n",
    "m_d_y=now.strftime(\"%m%d%y\")\n",
    "website='https://www.indiatoday.in/'\n",
    "path=r'C:\\Users\\Administrator\\Downloads\\chromedriver-win64\\my.py\\my.py.exe'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "3f57d42e-d9cd-4750-96f1-202fa2e3135a",
   "metadata": {},
   "outputs": [],
   "source": [
    "options=Options()\n",
    "options.headless=True\n",
    "service=Service(executable_path=path)\n",
    "driver=webdriver.Chrome(service=service)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "96a6b698-0376-4ad2-9c55-32a68336aef1",
   "metadata": {},
   "outputs": [],
   "source": [
    "driver.get(website)\n",
    "title=[]\n",
    "paragraph=[]\n",
    "link=[]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "cc09339e-db9d-4559-9055-7b1b1dac5e85",
   "metadata": {},
   "outputs": [],
   "source": [
    "containers=driver.find_elements(by=\"xpath\",value=\"//article[contains(@class,'B1S3_story__card__A_fhi')]\")\n",
    "for container in containers:\n",
    "    titles=container.find_element(by=\"xpath\",value=\".//h2/a\").text\n",
    "    paragraphs=container.find_element(by=\"xpath\",value=\".//p\").text\n",
    "    links=container.find_element(by=\"xpath\",value=\".//a\").get_attribute(\"href\")\n",
    "    title.append(titles)\n",
    "    paragraph.append(paragraphs)\n",
    "    link.append(links)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "d1f01745-fe92-486b-b420-1849a8641762",
   "metadata": {},
   "outputs": [],
   "source": [
    "my_dict={'titles': title,'paras': paragraph,'links': link}\n",
    "df_headlines=pd.DataFrame(my_dict)\n",
    "file_name=f'{app_path}/headless-{m_d_y}.csv'\n",
    "final_path=os.path.join(app_path,file_name)\n",
    "df_headlines.to_csv(final_path,index=False)\n",
    "driver.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "5020a5ea-6bdc-4b7c-b088-af92c9e5b248",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "4235 INFO: PyInstaller: 6.14.0, contrib hooks: 2025.4\n",
      "4235 INFO: Python: 3.12.3 (conda)\n",
      "4269 INFO: Platform: Windows-11-10.0.22631-SP0\n",
      "4269 INFO: Python environment: C:\\Users\\Administrator\\anaconda3\n",
      "4269 INFO: wrote C:\\Users\\Administrator\\auto1.spec\n",
      "4279 INFO: Module search paths (PYTHONPATH):\n",
      "['C:\\\\Users\\\\Administrator\\\\anaconda3\\\\Scripts\\\\pyinstaller.exe',\n",
      " 'C:\\\\Users\\\\Administrator\\\\anaconda3\\\\python312.zip',\n",
      " 'C:\\\\Users\\\\Administrator\\\\anaconda3\\\\DLLs',\n",
      " 'C:\\\\Users\\\\Administrator\\\\anaconda3\\\\Lib',\n",
      " 'C:\\\\Users\\\\Administrator\\\\anaconda3',\n",
      " 'C:\\\\Users\\\\Administrator\\\\anaconda3\\\\Lib\\\\site-packages',\n",
      " 'C:\\\\Users\\\\Administrator\\\\anaconda3\\\\Lib\\\\site-packages\\\\win32',\n",
      " 'C:\\\\Users\\\\Administrator\\\\anaconda3\\\\Lib\\\\site-packages\\\\win32\\\\lib',\n",
      " 'C:\\\\Users\\\\Administrator\\\\anaconda3\\\\Lib\\\\site-packages\\\\Pythonwin',\n",
      " 'C:\\\\Users\\\\Administrator\\\\anaconda3\\\\Lib\\\\site-packages\\\\setuptools\\\\_vendor',\n",
      " 'C:\\\\Users\\\\Administrator']\n",
      "8864 INFO: checking Analysis\n",
      "8905 INFO: checking PYZ\n",
      "8915 INFO: checking PKG\n",
      "8925 INFO: Bootloader C:\\Users\\Administrator\\anaconda3\\Lib\\site-packages\\PyInstaller\\bootloader\\Windows-64bit-intel\\run.exe\n",
      "8925 INFO: checking EXE\n",
      "8925 INFO: Build complete! The results are available in: C:\\Users\\Administrator\\dist\n"
     ]
    }
   ],
   "source": [
    "!pyinstaller --onefile auto1.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "29a18fd2-ef51-4319-99cb-3879d671c4da",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
