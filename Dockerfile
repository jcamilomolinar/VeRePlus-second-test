FROM node:18-alpine

WORKDIR /frontend

COPY package.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 9000

CMD ["npm", "run", "start"]

FROM python:3.10-alpine

WORKDIR /backend

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "index.py"]