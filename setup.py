from setuptools import setup, find_packages

setup(name='nonebot_plugin_admin_hello',
      version='0.6.3',
      description='nonebot plugin admin hello',
      long_description=open('README.md', 'r', encoding='utf-8').read(),
      long_description_content_type='text/markdown',
      author='HuYihe',
      author_email='2812856215@qq.com',
      packages=find_packages(),  # 系统自动从当前目录开始找包

      requires=['aiofiles',
                'fuzzyfinder',
                'httpx',
                'jieba',
                'nonebot_adapter_onebot',
                'nonebot2',
                'tencentcloud_sdk_python',
                'setuptools',
                'jinja2',
                'pyppeteer',
                'imageio',
                'numpy',
                'nonebot_plugin_apscheduler',
                'nonebot_plugin_htmlrender',
                'beautifulsoup4',
                'httpx',
                'lxml',
                'Pillow',
                'matplotlib',
                'xlsxwriter',
                'sqlitedict',
                'aiofiles',
                'littlepaimon_utils',
                'requests',
                'pydantic',
                ],
      )
