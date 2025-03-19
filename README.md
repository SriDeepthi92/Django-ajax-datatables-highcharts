
# Datatables using DataTables.net & Highcharts example
## This is an examples of a Ajax datatables and Highcharts implementation for a django project.

### Dependencies
Django==4.2.16

django-ajax-datatable==4.4.2

djangorestframework 3.9.0

#### Getting Started

First thing is to clone the project into the folder you want to work from. git clonehttps://github.com/SriDeepthi92/Django-ajax-datatables-highcharts


Then we need to create a virtual environment to install the dependencies. virtualenv env


Activate the virtual environment. For windows run: ./env/Scripts/activate



For linux: source env/bin/activate

#### Installing
Install the requirements. pip install -r requirements.txt

Install the package by running:

pip install django-ajax-datatable

then add 'ajax_datatable' to your INSTALLED_APPS:

INSTALLED_APPS = [

    ...
    'ajax_datatable',
]

### Setting up Django
CD into the myproject folder. cd myproject


Run migrate to set up the database. python manage.py migrate


Create a superuser so we can add rows to the database. python manage.py createsuperuser


Run the app. python manage.py runserver


Using the app
Go into the admin to create a table so we have something to view. 127.0.0.1:8000/admin


Now you can navigate to 127.0.0.1:8000 to view the table.

Pre-requisites
--------------

Your base template should include what required by `datatables.net`, plus:

- /static/ajax_datatable/css/style.css
- /static/ajax_datatable/js/utils.js

Example (plain jQuery from CDN):

.. code:: html

    {% block extrastyle %}

        <link href="{% static 'ajax_datatable/css/style.css' %}" rel="stylesheet" />
        <link href="//cdn.datatables.net/1.10.22/css/jquery.dataTables.min.css" />

    {% endblock extrastyle %}

    {% block extrajs %}

        <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
        <script type="text/javascript" src="{% static 'ajax_datatable/js/utils.js' %}"></script>
        <script src="//cdn.datatables.net/1.10.22/js/jquery.dataTables.min.js"></script>

    {% endcompress %}


Example (with Bootstrap4 support):

.. code:: html

    {% block extrastyle %}

        <link href="{% static 'ajax_datatable/css/style.css' %}" rel="stylesheet" />
        <!-- link rel='stylesheet' href="{% static 'datatables.net-bs/css/dataTables.bootstrap.min.css' %}" -->
        <link rel='stylesheet' href="{% static 'datatables.net-bs4/css/dataTables.bootstrap4.min.css' %}">
        <link rel='stylesheet' href="{% static 'datatables.net-buttons-bs/css/buttons.bootstrap.min.css' %}">
        <link rel='stylesheet' href="{% static 'https://code.highcharts.com/css/highcharts.css">' %}">

    {% endblock extrastyle %}

    {% block extrajs %}
        <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/select/3.0.0/js/dataTables.select.js"></script>
        <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/select/3.0.0/js/select.dataTables.js"></script>
        <script type="text/javascript" charset="utf8" src="https://code.jquery.com/jquery-3.7.1.js"></script>
        <script type="text/javascript" src="{% static 'ajax_datatable/js/utils.js' %}"></script>
        <script type="text/javascript" src="https://code.highcharts.com/highcharts.js"></script>
        <script src="{% static 'datatables.net/js/jquery.dataTables.min.js' %}"></script>
        <!-- script src="{% static 'datatables.net-bs/js/dataTables.bootstrap.min.js' %}"></script -->
        <script src="{% static 'datatables.net-bs4/js/dataTables.bootstrap4.min.js' %}"></script>
        <script src="{% static 'datatables.net-buttons/js/dataTables.buttons.min.js' %}"></script>
        <script src="{% static 'datatables.net-buttons/js/buttons.print.min.js' %}"></script>
        <script src="{% static 'datatables.net-buttons/js/buttons.html5.min.js' %}"></script>
        <script src="{% static 'datatables.net-buttons-bs/js/buttons.bootstrap.min.js' %}"></script>
        <script src="{% static 'jszip/dist/jszip.min.js' %}"></script>
        <script src="{% static 'pdfmake/build/pdfmake.min.js' %}"></script>
        <script src="{% static 'pdfmake/build/vfs_fonts.js' %}"></script>

    {% endcompress %}



#### Base configuration

Linux machine

Problem with vmware share folders

- if no folder exists in `/mnt/` create `hgfs` folder:
  `sudo mkdir hgfs`
- allow ports to communciate with the command:
  `sudo vmhgfs-fuse .host:/ /mnt/hgfs/ -o allow_other -o uid=1000`


#### Django installation

Install Django

`python -m pip install Django`

Install Django restframework

`python -m pip install djangorestframework`

Install requirements.txt

`python -m pip install requirements.txt`

Install psycopg2

`python -m pip install psycopg2-binary`

Install computer-property module for Django

`python -m pip install django-computed-property`

Install django_tables2 module for Django

`python -m pip install django-tables2`

Install computedfields module for Django

`pip install django-computedfields`

---

`django-admin startproject project_name . `

`python manage.py runserver`

Add notes for creating superuser

`python3 manage.py makemigrations` to connect the classes in the app files to the database

`python3 manage.py migrate` after making migrations apply those migrations to the webpage
`python3 manage.py createsuperuser` 

Events triggers sent directly by DataTables.net are listed here:

    https://datatables.net/reference/event/

#### Sample code:

    ..code :: html

     <div id="column-chart-container" style="width: 100%"></div>
    <div class="container">

    <table class="table" id="data-table" style="position: relative;">


     <script>
    $(document).ready( function () {
	new DataTable('#data-table', {
    search: {
        return: true
        }
        });
        });
    </script>

     <!-- Highcharts Script -->
     <script>
        function getDataFromTable(tableId) {
            const table = document.getElementById(tableId);
            const rows = table.querySelectorAll("tbody tr");
            const categories = [];
            const values = [];

            rows.forEach(row => {
                const cells = row.querySelectorAll("td");
                categories.push(cells[1].innerText); // Categories
                values.push(parseFloat(cells[4].innerText.trim())); // Values
            });

            return { categories, values };
        }

        const data = getDataFromTable("data-table");

        Highcharts.chart('column-chart-container', {
            chart: {
                type: 'column'
            },
            title: {
                text: 'Zero Carbon Rate by Fuel Type'
            },
            xAxis: {
                categories: data.categories,
                title: {
                    text: 'Fuel Type'
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Zero Carbon Rate'
                }
            },
            series: [{
                name: 'Carbon Rates',
                data: data.values
            }]
        });
    </script>


##### Git commands

    <u> Important commands </u>

```
git init
git status
git add  .
git commit -m “message”
git log –oneline
git reset //commit_number// --hard
git branch branchName
git branch -a (*means you’re on that branch)
git checkout branchName
git branch -D branchName (deletes branch)
git checkout -b branchName (checkout + create new branch)
git checkout master 🡪git merge branchName (merge branchName to merge)
```

