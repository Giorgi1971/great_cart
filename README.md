# great_cart
* From Vitali udemy.com account e-commerce Django.
* Python3 -m venv env
* Source env/bin/activate 
* pip install Django==4.1
* Django-admin startproject great_cart . (წერტილი სჭირდება რათა ამ საქაღალდეში შეიქმნას პროექტი)

## პროექტის შესახებ
უდემის კურსი e-commerce. ვიტალის აქვს ნაყიდი. 
აქვს უზერ კლასის გადატვირთვა. რეგისტრაციის ფორმით გაკეთება. მეილით აქვიზაცია. ასევე უსაფრთხოების დაცვა და AWS-ზე ატვირთვა.
ასევე პაიპალის გადახდების დამატება, მე ამ ჯერზე არ ვაკეთებ.


#### რათა სენეიტიური ინფორმაცია დავმალოთ 
* pip install python-decouple
* create .env file in project folder
* DEBUG=True // (without space in .env file)
* DEBUG = config('config') // in settings.py

#### admin გვერდის ფეიკი
* pip install django-admin-honeypot
* INSTALLED_ARR -> 'admin_honeypot'
* admin.urls-სი ცვლილებები
