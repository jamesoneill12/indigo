from django_assets import Bundle, register

register('css', Bundle(
    'bower_components/bootstrap/dist/css/bootstrap.min.css',
    'bower_components/bootstrap/dist/css/bootstrap-theme.min.css',
    Bundle(
        'stylesheets/*.scss',
        filters='pyscss',
        output='stylesheets/styles.%(version)s.css'),
    output='stylesheets/app.%(version)s.css'))

register('js', Bundle(
    'bower_components/jquery/dist/jquery.min.js',
    'javascript/*.js',
    output='javascript/app.%(version)s.js'))
