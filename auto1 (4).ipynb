{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "07c32d63-b37c-4eb2-9868-fc8a40c5f36e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "from selenium.webdriver.chrome.service import Service\n",
    "from selenium.webdriver.chrome.options import Options\n",
    "import pandas as pd\n",
    "import os\n",
    "import sys\n",
    "from datetime import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "89186f76-0dcb-440b-a260-039fdb84660f",
   "metadata": {},
   "outputs": [],
   "source": [
    "app_path=os.path.dirname(sys.executable)\n",
    "now=datetime.now()\n",
    "m_d_y=now.strftime(\"%m%d%y\")\n",
    "path=r'C:\\Users\\Administrator\\Downloads\\chromedriver-win64\\my.py\\my.py.exe'\n",
    "website = 'https://www.indiatoday.in/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "38ad187b-6ab8-4d2f-ae79-1ef9aa0f5b57",
   "metadata": {},
   "outputs": [],
   "source": [
    "options=Options()\n",
    "options.headless=True    \n",
    "service=Service(executable_path=path)\n",
    "driver=webdriver.Chrome(service=service,options=options)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b8240997-416d-445e-b357-d27e1126f076",
   "metadata": {},
   "outputs": [],
   "source": [
    "driver.get(website)\n",
    "containers=driver.find_elements(by='xpath',value=\"//article[contains(@class,'B1S3_story__card__A_fhi')]\")\n",
    "titles=[]\n",
    "paragraphs=[]\n",
    "links=[]\n",
    "for container in containers:\n",
    "    title = container.find_element(by=\"xpath\",value=\".//h2/a\").text\n",
    "    para = container.find_element(by=\"xpath\",value=\".//p\").text\n",
    "    link = container.find_element(by=\"xpath\",value=\".//a\").get_attribute(\"href\")\n",
    "    titles.append(title)\n",
    "    paragraphs.append(para)\n",
    "    links.append(link)\n",
    "\n",
    "my_dict={'title':titles,'paras': paragraphs,'link':links}\n",
    "df_headlines = pd.DataFrame(my_dict)\n",
    "file_name=f'{app_path}/headless-{m_d_y}.csv'\n",
    "final_path=os.path.join(app_path, file_name)\n",
    "df_headlines.to_csv(final_path,index=False)\n",
    "driver.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b1fd0499-6c93-4a6c-ba17-104c5a634141",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "7127 INFO: PyInstaller: 6.14.0, contrib hooks: 2025.4\n",
      "7127 INFO: Python: 3.12.3 (conda)\n",
      "7188 INFO: Platform: Windows-11-10.0.22631-SP0\n",
      "7188 INFO: Python environment: C:\\Users\\Administrator\\anaconda3\n",
      "7188 INFO: wrote C:\\Users\\Administrator\\auto1.spec\n",
      "7215 INFO: Module search paths (PYTHONPATH):\n",
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
      "14624 INFO: checking Analysis\n",
      "14746 INFO: checking PYZ\n",
      "14809 INFO: checking PKG\n",
      "14838 INFO: Bootloader C:\\Users\\Administrator\\anaconda3\\Lib\\site-packages\\PyInstaller\\bootloader\\Windows-64bit-intel\\run.exe\n",
      "14838 INFO: checking EXE\n",
      "14869 INFO: Build complete! The results are available in: C:\\Users\\Administrator\\dist\n"
     ]
    }
   ],
   "source": [
    "!pyinstaller --onefile auto1.py"
   ]
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
