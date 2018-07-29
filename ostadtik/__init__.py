from flask_sqlalchemy import SQLAlchemy

__author__ = "NOROUZI"

db = SQLAlchemy()


def create_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
    from ostadtik.Calltime.api import calltime as calltime_blueprint
    app.register_blueprint(calltime_blueprint)
    from ostadtik.comment.api import comment_blueprint
    app.register_blueprint(comment_blueprint)
    from ostadtik.course.api import course as course_blueprint
    app.register_blueprint(course_blueprint)
    from ostadtik.Student.api import student as student_blueprint
    app.register_blueprint(student_blueprint)
    from ostadtik.teacher.api import teacher as teacher_blueprint
    app.register_blueprint(teacher_blueprint)
    from ostadtik.profile.api import profile as profile_blueprint
    app.register_blueprint(profile_blueprint)
    from ostadtik.Class.api import classtable as class_blueprint
    app.register_blueprint(class_blueprint)

    return app
