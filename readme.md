# Arlington

A Django blog app.


## Installation

### Add project to Python path

`add2virtualenv arlington/arlington`

### Flatpages

Load a default "about" page.

```
cdproject; django-admin.py loaddata arlington/flatpages/fixtures/default.json
```

### Misc

Fill in the `<meta>` description of your website in the `base.html` template.
  
```
arlington/templates/base.html
```