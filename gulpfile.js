var gulp = require('gulp');
var sass = require('gulp-sass');


var PATHS = {
    SASS: {
        SRC: 'scss/**/*.scss',
        DIST: 'static/css'
    }
}


gulp.task('sass-dev', function () {
    var opts = {};

    return gulp.src(PATHS.SASS.SRC)
        .pipe(sass(opts))
        .pipe(gulp.dest(PATHS.SASS.DIST));
});


gulp.task('watch', function () {
    gulp.watch(PATHS.SASS.SRC, ['sass-dev']);
})
