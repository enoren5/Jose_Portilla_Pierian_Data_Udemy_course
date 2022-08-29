# <center>[Django 4 and Python Full-Stack Developer Masterclass](https://www.udemy.com/course/django-and-python-full-stack-developer-masterclass/)</center>
## <center>By Jose Portilla<center>

### About this course
#### Learn the entire technology stack to create beautiful and responsive websites with Python and Django!

## <center>Study Notes</center>
#### <center>Notes to self for personal reference</center>

## MISSING IN ACTION:
Sections (to be re watched and to take notes):
- 8
- 9
- 10 
- Filters: Lecture 63
 
## Section 10: Lecture 60: Variables
With this global variable declared inside views.py:

```
my_var = {
        'first_name': 'aleister',
        'last_name': 'crowley',
        'author_list': ['Paul F. Case','Arthur E. Waite','Manly P. Hall','Aleister Crowley',],
        'some_dict': {'inside_key':'inside_value'},
        'user_logged_in': False,
        'some_letter_list': ['a','b','c','d','e','f','g','h','i']
        }
```

To access "Arthur E Waite" and print it out on a web page, proper Jinja syntax would be:

```
 <h3>{{author_list.1}}</h3>
```

Take note above that the after the Key is referenced, the next operation to pull the list index value is separated by a dot (`.`).  For a regular Python script, square brackets are required to point to an index position in the list. But with Jinja, it's the Value name for the dictionary, a `.` to indicate the next operation, and then the index number. No square brackets.

## Section 11: Lecture 74: Data Interaction: Creating and Inserting

Three different ways to add data to a Django database .

Django Python shell:
### FIRST WAY: 
```
In [2]: from office.models import Patient
```
#### Instantiate's class as object:
```
In [3]: carl=Patient(first_name='Carl', last_name='Smith', age=25)
```
#### Saves above object to db:
```
In [4]: carl.save()
```
### SECOND WAY :
#### Creates and saves entry in db:
```
In [5]: Patient.objects.create(first_name='Susan', last_name='Smith', age=33)
Out[5]: <Patient: Patient object (2)>
```
#### Creates and saves entry in db:
```
In [6]: Patient.objects.create(first_name='mimi', last_name='bolus', age=36)
Out[6]: <Patient: Patient object (3)>
```

### THIRD WAY :
From the official Django Docs: [bulk_create()](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#bulk-create). Live demo:

```
In [7]: mylist=[Patient(first_name='mimi', last_name='bolus', age=36),Patient(first_name='Karl', last_name='Marx', age=37)]

In [8]: Patient.objects.bulk_create(mylist)
Out[8]: [<Patient: Patient object (4)>, <Patient: Patient object (5)>]
```

### MORE :
Based on my forum thread from a few weeks ago titled "[Database entry changes to ‘polling’ web app from official Django docs](https://forum.djangoproject.com/t/database-entry-changes-to-polling-web-app-from-official-django-docs/14595/4)"
If I accidentally input incorrect data and wish to alter an existing entry in my db tables, I can use this:

```
>>> c = Patient.objects.get(pk=4) # or which ever pk (primary key you want to grab)
>>> c.first_name = 'Joseph'
>>> c.last_name = 'Smith'
>>> c.save()
```
## MORE : Section 11: Lectures 76, 77, 78, 79, 80, 81 :
Additional notes on Querying DB can be found in `office/views.py` and `office/templates/office/list.html`
Those annotations cover material involving how to interface and interact with database in views and templates instead of Django shell

## Section 12 : "Django Admin"
What Jose Portilla called 'cars' app, I more accurately named it a 'dealership' app.
Not only does this Section cover how to wire up model data to Django Admin but Jose also demonstrates how to Create, Read, Update, and Delete data in the database in `views.py` with templates. This app accepts web visitor car `brand` and `year` input, lists it, and gives an option to delete based on Django `pk` identifier.

## Section 13 : "Django Forms" (cookie cutter built-in forms)
For Jose Portilla's next app, he called it 'cars' again. But I named it 'car_rentals' since it's a basic website which accepts web visitor input to review the cars that they rented.

## Section 13 : Lecture 91 : Widgets and Styling :
Here is a sample from `forms.py`:
```
    review = forms.CharField(
        label="Your comments go here", 
        max_length=500,
        widget=forms.Textarea(attrs={
                'class':'myform', 
                'rows':'25',
                'cols':'25'}
                )
        )
```
Above you can see the `review` class attribute is a form input box that carries three arguments: (1) label, (2) max_length, and (3) a "widget"
Here is the official Django documentation covering widgets but [specific to Textarea](https://docs.djangoproject.com/en/4.1/ref/forms/widgets/#textarea). The next argument is `attrs` which refers to the input box HTML tag attributes. The argument is a `dict()` type. There is `class` key and paired with  `myform` value which is a CSS class attribute (not to be confused with Python class attributes) that is located inside the newly created `custom.css` file which is stored in the app's `static` directory. The next item in the dictionary is `rows` key with `25` value that specifies the size of the input box. Take note that when Django serves the `rental_review.html`, the dashed red border surrounds the `review` input box because of how the `widget` argument is being formatted.