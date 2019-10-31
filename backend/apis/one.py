from flask_restplus import Namespace, Resource
from backend.core.one_helloworld import OneHelloWorld


ns = Namespace('backend/one', description='Python Web Framework of HelloWorld')

one_hello = OneHelloWorld()


@ns.route('/test/<message>', endpoint='test')
@ns.doc(params={'message': 'Input message'})
@ns.response(404, 'fun not found')
class HelloOne(Resource):
    @ns.doc('get message')
    def get(self, message):
        return one_hello.get(message)


    @ns.doc('put message')
    def post(self, message):
        return one_hello.put(message)

