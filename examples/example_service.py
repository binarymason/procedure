from procedure import Procedure
from procedure.service import Service

class ExampleProcedure(Procedure):
    def run(self):
        print("Running a procedure!")
        print(self.ctx._kwargs)

class ExampleService(Service):
    def parse_request_args(self, request):
        return { "foo": "bar", "params": dict(request.args)}


if __name__ == '__main__':
    ExampleService.call(procedure=ExampleProcedure, port=3333, host='0.0.0.0', debug=True)

