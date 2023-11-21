FROM python:3.8

# streamlit-specific commands
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'
RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
enableXsrfProtection=false\n\
" > /root/.streamlit/config.toml'


EXPOSE 8501
COPY . ./app
RUN pip3 --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org install -r app/requirements.txt

COPY . .
CMD streamlit run app/app.py --server.enableCORS=false server.enableXsrfProtection=false --server.headless=true --global.developmentMode=false --server.port="8501"