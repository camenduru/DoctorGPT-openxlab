import os
os.chdir(f"/home/xlab-app-center")
os.system(f"git clone -b v2.1 https://github.com/camenduru/text-generation-webui /home/xlab-app-center/text-generation-webui")
os.chdir(f"/home/xlab-app-center/text-generation-webui")
os.system(f"git lfs install")
os.system(f"git reset --hard")

os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/camenduru/medllama2_7b/weight//pytorch_model-00001-of-00002.bin -d /home/xlab-app-center/text-generation-webui/models/medllama2_7b -o pytorch_model-00001-of-00002.bin")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/camenduru/medllama2_7b/weight//pytorch_model-00002-of-00002.bin -d /home/xlab-app-center/text-generation-webui/models/medllama2_7b -o pytorch_model-00002-of-00002.bin")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/camenduru/medllama2_7b/weight//config.json -d /home/xlab-app-center/text-generation-webui/models/medllama2_7b -o config.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/camenduru/medllama2_7b/weight//generation_config.json -d /home/xlab-app-center/text-generation-webui/models/medllama2_7b -o generation_config.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/camenduru/medllama2_7b/weight//pytorch_model.bin.index.json -d /home/xlab-app-center/text-generation-webui/models/medllama2_7b -o pytorch_model.bin.index.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/camenduru/medllama2_7b/weight//special_tokens_map.json -d /home/xlab-app-center/text-generation-webui/models/medllama2_7b -o special_tokens_map.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/camenduru/medllama2_7b/weight//tokenizer.json -d /home/xlab-app-center/text-generation-webui/models/medllama2_7b -o tokenizer.json")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/camenduru/medllama2_7b/weight//tokenizer_config.json -d /home/xlab-app-center/text-generation-webui/models/medllama2_7b -o tokenizer_config.json")

os.system(f"python server.py --share --model /home/xlab-app-center/text-generation-webui/models/medllama2_7b")
