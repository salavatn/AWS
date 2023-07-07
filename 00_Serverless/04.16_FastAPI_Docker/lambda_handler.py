import mangum
from webapp import app

handler = mangum.Mangum(app)
# handler.handler