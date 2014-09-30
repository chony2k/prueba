The project is hosted at https://github.com/chony2k/prueba

It contains the following links

	 - A view/URL that accept a date and return the matching phrases.

		This view is rather simple, it renders a form with two fields, day and month, on submittion, the filter is applied by using Django's QuerySet
		features.

	- A view or Python script to import the CSV content into the database.

	    A python script was created to do this. It leverages the CSV library, which speed up the process of splitting lines into discrete values.
	    To run the script, open a shell console in the root of the prohject and type python importer.py  

	    Before running the script, edit it and update the path to your project.


	- A view to calculate the the total number of words in the phrases.

	   For this requirement, it was assumed that it meat total words PER phrase, so a list of phrases is
	   displayed with the corresponding title and word count. The word count is calculated by splitting the
	   phrase body into words and then calling len() in the resulting list.

	- Incorporate Django-tagging into the app: https://github.com/alex/django-taggit

	   When editing / adding phrases through the django admin tool, you will see a field for the tags. This is an area for further work, since the tags
	   could be nicely shown in all the listings. 

	- A view that using phrases as a list two elements secuences of strings, detects which elements are string's rotation 

	  The view works by firstly separating each phrase body into subsets of two, then applying a is_rotation function
	  to come up with he phrases that match the condition.

	  Notice that if two words are the same, we assume that one is a valid rotation of the other.


To install the project:

    1. Clone de repo
    2. Create a virtualenv and type:  pip install -r requirements.pip
    3. Run syncdb and migrate so that tables are created
    4. Edit the importer.php and update the path in it to match your system's characteristics
    5. Run the importer: python importer.py
    6. Start the server: python manage.py runserver
    7. Point your browser to localhost:8000/mysite







	
