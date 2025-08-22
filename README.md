Flask Blog Application

This is a simple Flask-based blog application that allows users to create, update, delete, like, and dislike blog posts. 
The data is stored in a JSON file. You can use the Buttons or the routes below for the URL.

Routes:

    •	/ – Display all blog posts with like/dislike and update/delete options.
	•	/add – Create a new blog post (GET shows the form, POST saves the post).
	•	/update/<int:post_id> – Update an existing post by its ID.
	•	/delete/<int:post_id> – Delete a post by its ID.
	•	/like/<int:post_id> – Increment the like counter of a post.
	•	/dislike/<int:post_id> – Increment the dislike counter of a post.

    