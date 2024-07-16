-------------------------------------------------Technial_Test_API_Personas-------------------------------------------------

Gestionador de API de personas.

Base de datos: Sqlite3 (ya que se tiene una aplicación pequeña, esta base de datos es idonea, en caso que se escale a una aplicación más grande, se realiaría el cambio de base de datos)
Framework: Django Rest FrameWork (DRF)

1) Tener 100 personas registradas en base de datos
R/= Para este punto se crea un script el cual al inicia la aplicación, en este caso, cada vez que ejecutamos py manage.py runserver, se ejecuta este script cargando la la base de datos con 100 registro. Para obtener la información de los registro se utilizo del pacuete Faker.

 Antes de iniciar la aplicación
 
 ![image](https://github.com/socratess/Technial_Test_API_Personas/assets/25992143/af370a68-5d9b-4567-b095-2a317b3aa582)

 Al iniciar la aplicación
 
![image](https://github.com/socratess/Technial_Test_API_Personas/assets/25992143/a357409e-1c3a-4f8f-b6d7-72032796ddc9)

Despues de iniciar la aplicación

![image](https://github.com/socratess/Technial_Test_API_Personas/assets/25992143/4317bcd4-624c-4732-b4ec-cdb396e2fae4)

El script el cual se hizó mención previamente se llama data.py
![image](https://github.com/socratess/Technial_Test_API_Personas/assets/25992143/1300ab47-f1b0-43da-8e64-d6d1d4fda743)

 2) Agregar vista Swager
    ![image](https://github.com/socratess/Technial_Test_API_Personas/assets/25992143/ad3d504b-6948-4929-8131-aa9591348605)

3) Modelo con los siguientes datos de la persona:
   Datos de la persona
-Nombre
-Apellido
-Celular
-Correo
  ![image](https://github.com/socratess/Technial_Test_API_Personas/assets/25992143/8da9f3e2-14f7-4e9c-8d31-1d6196c30f1f)

![image](https://github.com/socratess/Technial_Test_API_Personas/assets/25992143/7fb3b82c-4504-4e7d-8229-da6b2637d9f9)


5) Realizar una api que me entrege un GET, POST, GET/ID
   ![image](https://github.com/socratess/Technial_Test_API_Personas/assets/25992143/5f29f91a-a9da-43a7-8ac6-edcafe85fc40)

GET:
![image](https://github.com/socratess/Technial_Test_API_Personas/assets/25992143/e1f13c31-7798-4a7b-9e59-d7164d077a4b)

POST:
![image](https://github.com/socratess/Technial_Test_API_Personas/assets/25992143/7f82402f-712d-446e-b368-dc97ccad8e36)

GET/ID
![image](https://github.com/socratess/Technial_Test_API_Personas/assets/25992143/026c2499-1021-4224-a37d-442d7f26d566)

5) con el GET traer lista de 10 personas con paginación. ademas, poder decidir si trae las 100 personas
   
GET traer lista de 10 personas con paginación
![image](https://github.com/socratess/Technial_Test_API_Personas/assets/25992143/f54726da-b005-494d-a1e1-4e4c28b6c7e1)

Poder decidir si trae las 100 personas
![image](https://github.com/socratess/Technial_Test_API_Personas/assets/25992143/9e296bf1-644d-4075-ac1d-318037c1021c)

Con todo lo anterior, se da entrega a los requerimientos solicitados. 
