FROM python
WORKDIR /app
COPY . /app
RUN pip3 install discord.py
RUN pip3 install boto3
RUN pip3 install mcstatus
RUN pip3 install python-dotenv
CMD ["python3", "run.py"]