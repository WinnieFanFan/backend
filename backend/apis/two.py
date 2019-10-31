from flask_restplus import Namespace, Resource
from backend.core.two_helloworld import TwoHelloWorld


ns = Namespace('backend/two', description='Python Web Framework of HelloWorld')

two_hello = TwoHelloWorld()


@ns.route('/test2/<id>', endpoint='test2')
@ns.doc(params={'id': 'Input ID'})
@ns.response(404, 'fun not found')
class HelloTwo(Resource):
    @ns.doc('get ID')
    def get(self, id):
        return two_hello.run(id)


    @ns.doc('put id')
    def post(self, id):
        return two_hello.run(id)
