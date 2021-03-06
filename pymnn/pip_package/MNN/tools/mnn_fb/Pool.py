# automatically generated by the FlatBuffers compiler, do not modify

# namespace: MNN

import flatbuffers

class Pool(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPool(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Pool()
        x.Init(buf, n + offset)
        return x

    # Pool
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Pool
    def PadX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Pool
    def PadY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Pool
    def IsGlobal(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # Pool
    def KernelX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Pool
    def KernelY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Pool
    def StrideX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Pool
    def StrideY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Pool
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # Pool
    def PadType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # Pool
    def DataType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 1

    # Pool
    def CeilModel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return True

def PoolStart(builder): builder.StartObject(11)
def PoolAddPadX(builder, padX): builder.PrependInt32Slot(0, padX, 0)
def PoolAddPadY(builder, padY): builder.PrependInt32Slot(1, padY, 0)
def PoolAddIsGlobal(builder, isGlobal): builder.PrependBoolSlot(2, isGlobal, 0)
def PoolAddKernelX(builder, kernelX): builder.PrependInt32Slot(3, kernelX, 0)
def PoolAddKernelY(builder, kernelY): builder.PrependInt32Slot(4, kernelY, 0)
def PoolAddStrideX(builder, strideX): builder.PrependInt32Slot(5, strideX, 0)
def PoolAddStrideY(builder, strideY): builder.PrependInt32Slot(6, strideY, 0)
def PoolAddType(builder, type): builder.PrependInt8Slot(7, type, 0)
def PoolAddPadType(builder, padType): builder.PrependInt8Slot(8, padType, 0)
def PoolAddDataType(builder, dataType): builder.PrependInt32Slot(9, dataType, 1)
def PoolAddCeilModel(builder, ceilModel): builder.PrependBoolSlot(10, ceilModel, 1)
def PoolEnd(builder): return builder.EndObject()
