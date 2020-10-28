import pystache

class Utils:
    @classmethod
    def get_info_from_tmpl(self, tmplate_path, dict):
        with open(tmplate_path) as f:
            tmp = f.read()
        return pystache.render(tmp, dict)