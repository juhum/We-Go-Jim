# We Go Jim
We Go Jim is a web application designed for students and their trainers. The application allows trainers to create personalized workouts for students and track their progress. It provides visualizations of their records for both students and trainers.

## Installation
To get started with this project, clone this repository using git:

```bash
git clone https://github.com/juhum/We-Go-Jim.git
```

Firstly, create the .env file in the config directory and enter your credentials following the example.

To run the project, navigate to the root directory and build docker image:

```bash
docker build -t we-go-jim .
```

Run Docker Container:

```bash
docker run -p 127.0.0.1:5000:5000 we-go-jim
```


Then you can access the app locally at 127.0.0.1:5000

## Usage

You can create new account as a student or trainer, then login. Students can receive personalized workouts from trainers, follow the personal records with visualization. Trainers can also create workouts for students and follow their records.


## Tech stack

- Python
- Flask
- HTML
- CSS
- Javascript
- AWS
- Terraform
- Docker



## You can also access the application under the following link:
http://wegojim.atrolabs.com:5000/



![showcase](https://github.com/juhum/We-Go-Jim/blob/master/showcase.gif)

## Created by

- [Adam Kuszczyński](https://github.com/juhum)
- [Daniel Adamiak](https://github.com/xd4niel)
- [Grzegorz Łoszewski](https://github.com/Atrolide)
- [TomColada](https://github.com/TomColada)
- [Enderrnator](https://github.com/Enderrnator)
- [TheShoto11](https://github.com/TheShoto11)
