import doc
import api

import justpy as jp

jp.Route('/', doc.Doc.serve)
jp.Route('/api', api.Api.serve)
jp.justpy()
