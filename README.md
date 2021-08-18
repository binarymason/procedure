# Procedure

This package makes it easy to use the Interactor Pattern in Python. If you want to read up on that, view the [slides](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) or watch [video](https://www.youtube.com/watch?v=o_TH-Y78tt4)


### Usage
```py

from procedure import Procedure

class ExampleProcedure(Procedure):
    def run(self):
        self.ctx.baz = "bang" # add data to ctx object

result = ExampleProcedure.call(foo="bar")
# => ExampleProcedureContext( baz='bang' failure=None foo='bar' status='success' success=True verbose=False )
```

More detailed example is in jupyter notebook [here](examples/procedure.ipynb)


### Installation

```
pip install procedure
```

### Development

Publish new version:
```
./script/publish
```
