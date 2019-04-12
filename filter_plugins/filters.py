import json

class FilterModule(object):
    ''' Ansible core jinja2 filters '''

    def filters(self):
        return {
            'transform_visualization' : self.transform_visualization,
            'transform_dashboard' : self.transform_dashboard
        }

    def transform_visualization(self, viz_spec):

        def _de(val):
            return json.dumps(val)

        rtn = viz_spec

        rtn['attributes']['visState'] = _de(rtn['attributes']['visState'])
        rtn['attributes']['kibanaSavedObjectMeta']['searchSourceJSON'] = _de(rtn['attributes']['kibanaSavedObjectMeta']['searchSourceJSON'])

        return rtn

    def transform_dashboard(self, dash_spec):

        def _de(val):
            return json.dumps(val)

        rtn = dash_spec

        rtn['attributes']['panelsJSON'] = _de(rtn['attributes']['panelsJSON'])
        rtn['attributes']['kibanaSavedObjectMeta']['searchSourceJSON'] = _de(rtn['attributes']['kibanaSavedObjectMeta']['searchSourceJSON'])

        return rtn
