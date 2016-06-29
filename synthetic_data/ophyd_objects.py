from ophyd.areadetector import DetectorBase, SingleTrigger, ADBase
from ophyd.areadetector.filestore_mixins import FileStorePluginBase

from ophyd import Device, Component as Cpt, Signal


class SoftCam(ADBase):
    array_size = Cpt(Signal, value=(10, 10))
    acquire = Cpt(Signal, value=0)
    image_mode = Cpt(Signal, value=0)
    port_name = Cpt(Signal, value='CAM')


class SynMod(FileStorePluginBase, Device):
    auto_increment = Cpt(Signal, value='Yes')
    array_counter = Cpt(Signal, value=0)
    auto_save = Cpt(Signal, value='Yes')
    num_capture = Cpt(Signal, value=0)
    capture = Cpt(Signal, value=0)

    file_path = Cpt(Signal, value='')
    file_name = Cpt(Signal, value='')
    file_template = Cpt(Signal, value='%s%s%d')
    file_number = Cpt(Signal, value=0)
    file_path_exists = Cpt(Signal, value=True)

    def __init__(self, *args, read_attrs=None, **kwargs):
        if read_attrs is None:
            read_attrs = []
        super().__init__(*args, read_attrs=read_attrs, **kwargs)

        self.filestore_spec = 'syn-mod'
        self._resource = None
        self._prev_resource = []

    def stage(self):
        super().stage()
        shape = self.parent.cam.array_size.get()
        self._resource = self.parent.filestore.insert_resource(
            self.filestore_spec, '', {'shape': shape})
        self._prev_resource.append(self._resource)

    def generate_datum(self, key, timestamp):
        uid = super().generate_datum(key, timestamp)
        i = next(self._point_counter)
        self.parent.filestore.insert_datum(self._resource, uid, {'n': i})
        return uid


class MyDetector(SingleTrigger, DetectorBase):
    cam = Cpt(SoftCam, '')
    synmod = Cpt(SynMod, '', write_path_template='')

    def trigger(self):
        status = super().trigger()
        self.cam.acquire.put(0)
        return status

    def __init__(self, *args, filestore, read_attrs=None, **kwargs):
        '''

        Parameters
        ----------
        filestore : FileStore
             A instance of a FileStore which can insert documents
        '''
        self.filestore = filestore
        if read_attrs is None:
            read_attrs = ['synmod']
        super().__init__(*args, read_attrs=read_attrs, **kwargs)
