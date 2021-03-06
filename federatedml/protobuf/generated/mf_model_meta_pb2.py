# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mf-model-meta.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mf-model-meta.proto',
  package='com.webank.ai.fate.core.mlmodel.buffer.mf',
  syntax='proto3',
  serialized_options=_b('B\020MFModelMetaProto'),
  serialized_pb=_b('\n\x13mf-model-meta.proto\x12)com.webank.ai.fate.core.mlmodel.buffer.mf\",\n\tEarlyStop\x12\x12\n\nearly_stop\x18\x01 \x01(\t\x12\x0b\n\x03\x65ps\x18\x02 \x01(\x01\",\n\tOptimizer\x12\x11\n\toptimizer\x18\x01 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x02 \x01(\t\"\xb5\x02\n\rHeteroMFParam\x12\x18\n\x10secure_aggregate\x18\x01 \x01(\x08\x12\x1f\n\x17\x61ggregate_every_n_epoch\x18\x02 \x01(\x05\x12\x12\n\nbatch_size\x18\x03 \x01(\x05\x12\x10\n\x08max_iter\x18\x04 \x01(\x05\x12H\n\nearly_stop\x18\x05 \x01(\x0b\x32\x34.com.webank.ai.fate.core.mlmodel.buffer.mf.EarlyStop\x12\x0f\n\x07metrics\x18\x06 \x03(\t\x12G\n\toptimizer\x18\x07 \x01(\x0b\x32\x34.com.webank.ai.fate.core.mlmodel.buffer.mf.Optimizer\x12\x0c\n\x04loss\x18\x08 \x01(\t\x12\x11\n\tembed_dim\x18\t \x01(\x05\"o\n\x0bMFModelMeta\x12\x16\n\x0e\x61ggregate_iter\x18\x01 \x01(\x05\x12H\n\x06params\x18\x64 \x01(\x0b\x32\x38.com.webank.ai.fate.core.mlmodel.buffer.mf.HeteroMFParamB\x12\x42\x10MFModelMetaProtob\x06proto3')
)




_EARLYSTOP = _descriptor.Descriptor(
  name='EarlyStop',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.mf.EarlyStop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='early_stop', full_name='com.webank.ai.fate.core.mlmodel.buffer.mf.EarlyStop.early_stop', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eps', full_name='com.webank.ai.fate.core.mlmodel.buffer.mf.EarlyStop.eps', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=110,
)


_OPTIMIZER = _descriptor.Descriptor(
  name='Optimizer',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.mf.Optimizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='optimizer', full_name='com.webank.ai.fate.core.mlmodel.buffer.mf.Optimizer.optimizer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='com.webank.ai.fate.core.mlmodel.buffer.mf.Optimizer.args', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=156,
)


_HETEROMFPARAM = _descriptor.Descriptor(
  name='HeteroMFParam',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.mf.HeteroMFParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='secure_aggregate', full_name='com.webank.ai.fate.core.mlmodel.buffer.mf.HeteroMFParam.secure_aggregate', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aggregate_every_n_epoch', full_name='com.webank.ai.fate.core.mlmodel.buffer.mf.HeteroMFParam.aggregate_every_n_epoch', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='com.webank.ai.fate.core.mlmodel.buffer.mf.HeteroMFParam.batch_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_iter', full_name='com.webank.ai.fate.core.mlmodel.buffer.mf.HeteroMFParam.max_iter', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='early_stop', full_name='com.webank.ai.fate.core.mlmodel.buffer.mf.HeteroMFParam.early_stop', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='com.webank.ai.fate.core.mlmodel.buffer.mf.HeteroMFParam.metrics', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='optimizer', full_name='com.webank.ai.fate.core.mlmodel.buffer.mf.HeteroMFParam.optimizer', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loss', full_name='com.webank.ai.fate.core.mlmodel.buffer.mf.HeteroMFParam.loss', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='embed_dim', full_name='com.webank.ai.fate.core.mlmodel.buffer.mf.HeteroMFParam.embed_dim', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=468,
)


_MFMODELMETA = _descriptor.Descriptor(
  name='MFModelMeta',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.mf.MFModelMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='aggregate_iter', full_name='com.webank.ai.fate.core.mlmodel.buffer.mf.MFModelMeta.aggregate_iter', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='com.webank.ai.fate.core.mlmodel.buffer.mf.MFModelMeta.params', index=1,
      number=100, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=470,
  serialized_end=581,
)

_HETEROMFPARAM.fields_by_name['early_stop'].message_type = _EARLYSTOP
_HETEROMFPARAM.fields_by_name['optimizer'].message_type = _OPTIMIZER
_MFMODELMETA.fields_by_name['params'].message_type = _HETEROMFPARAM
DESCRIPTOR.message_types_by_name['EarlyStop'] = _EARLYSTOP
DESCRIPTOR.message_types_by_name['Optimizer'] = _OPTIMIZER
DESCRIPTOR.message_types_by_name['HeteroMFParam'] = _HETEROMFPARAM
DESCRIPTOR.message_types_by_name['MFModelMeta'] = _MFMODELMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EarlyStop = _reflection.GeneratedProtocolMessageType('EarlyStop', (_message.Message,), dict(
  DESCRIPTOR = _EARLYSTOP,
  __module__ = 'mf_model_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.mf.EarlyStop)
  ))
_sym_db.RegisterMessage(EarlyStop)

Optimizer = _reflection.GeneratedProtocolMessageType('Optimizer', (_message.Message,), dict(
  DESCRIPTOR = _OPTIMIZER,
  __module__ = 'mf_model_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.mf.Optimizer)
  ))
_sym_db.RegisterMessage(Optimizer)

HeteroMFParam = _reflection.GeneratedProtocolMessageType('HeteroMFParam', (_message.Message,), dict(
  DESCRIPTOR = _HETEROMFPARAM,
  __module__ = 'mf_model_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.mf.HeteroMFParam)
  ))
_sym_db.RegisterMessage(HeteroMFParam)

MFModelMeta = _reflection.GeneratedProtocolMessageType('MFModelMeta', (_message.Message,), dict(
  DESCRIPTOR = _MFMODELMETA,
  __module__ = 'mf_model_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.mf.MFModelMeta)
  ))
_sym_db.RegisterMessage(MFModelMeta)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
