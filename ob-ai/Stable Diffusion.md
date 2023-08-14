((masterpiece,best quality)),1girl, solo, animal ears, rabbit, barefoot, knees up, dress, sitting, rabbit ears, short sleeves, looking at viewer, grass, short hair, smile, white hair, puffy sleeves, outdoors, puffy short sleeves, bangs, on ground, full body, animal, white dress, sunlight, brown eyes, dappled sunlight, day, depth of field

EasyNegative, extra fingers,fewer fingers


启动WebUI服务,左键点击生成的URL：[https://dsw-gateway-cn-shanghai.data.aliyun.com/dsw-257471/proxy/7860/](https://dsw-gateway-cn-shanghai.data.aliyun.com/dsw-257471/proxy/7860/) 跳转到WebUI前端  

! cd stable-diffusion-webui && python -m venv --system-site-packages --symlinks venv

! cd stable-diffusion-webui && \

  sed -i 's/can_run_as_root=0/can_run_as_root=1/g' webui.sh && \

  ./webui.sh --no-download-sd-model --xformers --gradio-queue