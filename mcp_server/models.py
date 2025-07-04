# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T01:07:49+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class PolicyApiLifecycleStage(Enum):
    API_UNSPECIFIED = 'API_UNSPECIFIED'
    API_PREVIEW = 'API_PREVIEW'
    API_DEVELOPMENT = 'API_DEVELOPMENT'
    API_CURRENT = 'API_CURRENT'
    API_DEPRECATED = 'API_DEPRECATED'


class GoogleChromePolicyVersionsV1AdditionalTargetKeyName(BaseModel):
    key: Optional[str] = Field(None, description='Key name.')
    keyDescription: Optional[str] = Field(None, description='Key description.')


class GoogleChromePolicyVersionsV1CertificateReference(BaseModel):
    network: Optional[str] = Field(
        None, description='Output only. The name of the referencing network.'
    )
    orgUnitId: Optional[str] = Field(
        None,
        description='Output only. The obfuscated id of the org unit the referencing network is in.',
    )


class GoogleChromePolicyVersionsV1NetworkSetting(BaseModel):
    policySchema: Optional[str] = Field(
        None, description='The fully qualified name of the network setting.'
    )
    value: Optional[Dict[str, Any]] = Field(
        None, description='The value of the network setting.'
    )


class GoogleChromePolicyVersionsV1NumericRangeConstraint(BaseModel):
    maximum: Optional[str] = Field(None, description='Maximum value.')
    minimum: Optional[str] = Field(None, description='Minimum value.')


class GoogleChromePolicyVersionsV1PolicyModificationFieldError(BaseModel):
    error: Optional[str] = Field(
        None, description='Output only. The error message related to the field.'
    )
    field: Optional[str] = Field(
        None, description='Output only. The name of the field with the error.'
    )


class ValidTargetResource(Enum):
    TARGET_RESOURCE_UNSPECIFIED = 'TARGET_RESOURCE_UNSPECIFIED'
    ORG_UNIT = 'ORG_UNIT'
    GROUP = 'GROUP'


class GoogleChromePolicyVersionsV1PolicySchemaFieldDependencies(BaseModel):
    sourceField: Optional[str] = Field(
        None, description='The source field which this field depends on.'
    )
    sourceFieldValue: Optional[str] = Field(
        None,
        description='The value which the source field must have for this field to be allowed to be set.',
    )


class GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescription(BaseModel):
    description: Optional[str] = Field(
        None, description='Output only. Additional description for this value.'
    )
    value: Optional[str] = Field(
        None,
        description='Output only. The string represenstation of the value that can be set for the field.',
    )


class GoogleChromePolicyVersionsV1PolicySchemaNoticeDescription(BaseModel):
    acknowledgementRequired: Optional[bool] = Field(
        None,
        description='Output only. Whether the user needs to acknowledge the notice message before the value can be set.',
    )
    field: Optional[str] = Field(
        None, description='Output only. The field name associated with the notice.'
    )
    noticeMessage: Optional[str] = Field(
        None,
        description='Output only. The notice message associate with the value of the field.',
    )
    noticeValue: Optional[str] = Field(
        None,
        description='Output only. The value of the field that has a notice. When setting the field to this value, the user may be required to acknowledge the notice message in order for the value to be set.',
    )


class GoogleChromePolicyVersionsV1PolicySchemaRequiredItems(BaseModel):
    fieldConditions: Optional[List[str]] = Field(
        None,
        description='The value(s) of the field that provoke required field enforcement. An empty field_conditions implies that any value assigned to this field will provoke required field enforcement.',
    )
    requiredFields: Optional[List[str]] = Field(
        None,
        description='The fields that are required as a consequence of the field conditions.',
    )


class GoogleChromePolicyVersionsV1PolicyTargetKey(BaseModel):
    additionalTargetKeys: Optional[Dict[str, str]] = Field(
        None,
        description='Map containing the additional target key name and value pairs used to further identify the target of the policy.',
    )
    targetResource: Optional[str] = Field(
        None,
        description='The target resource on which this policy is applied. The following resources are supported: * Organizational Unit ("orgunits/{orgunit_id}") * Group ("groups/{group_id}")',
    )


class GoogleChromePolicyVersionsV1PolicyValue(BaseModel):
    policySchema: Optional[str] = Field(
        None,
        description='The fully qualified name of the policy schema associated with this policy.',
    )
    value: Optional[Dict[str, Any]] = Field(
        None,
        description='The value of the policy that is compatible with the schema that it is associated with.',
    )


class GoogleChromePolicyVersionsV1RemoveCertificateErrorDetails(BaseModel):
    certificateReferences: Optional[
        List[GoogleChromePolicyVersionsV1CertificateReference]
    ] = Field(
        None,
        description='Output only. If the certificate was not removed, a list of references to the certificate that prevented it from being removed. Only unreferenced certificates can be removed.',
    )


class GoogleChromePolicyVersionsV1RemoveCertificateRequest(BaseModel):
    networkId: Optional[str] = Field(
        None, description='Required. The GUID of the certificate to remove.'
    )
    targetResource: Optional[str] = Field(
        None,
        description='Required. The target resource on which this certificate will be removed. The following resources are supported: * Organizational Unit ("orgunits/{orgunit_id}")',
    )


class GoogleChromePolicyVersionsV1RemoveCertificateResponse(BaseModel):
    pass


class GoogleChromePolicyVersionsV1RemoveNetworkRequest(BaseModel):
    networkId: Optional[str] = Field(
        None, description='Required. The GUID of the network to remove.'
    )
    targetResource: Optional[str] = Field(
        None,
        description='Required. The target resource on which this network will be removed. The following resources are supported: * Organizational Unit ("orgunits/{orgunit_id}")',
    )


class GoogleChromePolicyVersionsV1RemoveNetworkResponse(BaseModel):
    pass


class GoogleChromePolicyVersionsV1ResolveRequest(BaseModel):
    pageSize: Optional[int] = Field(
        None,
        description='The maximum number of policies to return, defaults to 100 and has a maximum of 1000.',
    )
    pageToken: Optional[str] = Field(
        None,
        description='The page token used to retrieve a specific page of the request.',
    )
    policySchemaFilter: Optional[str] = Field(
        None,
        description='Required. The schema filter to apply to the resolve request. Specify a schema name to view a particular schema, for example: chrome.users.ShowLogoutButton Wildcards are supported, but only in the leaf portion of the schema name. Wildcards cannot be used in namespace directly. Please read https://developers.google.com/chrome/policy/guides/policy-schemas for details on schema namespaces. For example: Valid: "chrome.users.*", "chrome.users.apps.*", "chrome.printers.*" Invalid: "*", "*.users", "chrome.*", "chrome.*.apps.*"',
    )
    policyTargetKey: Optional[GoogleChromePolicyVersionsV1PolicyTargetKey] = Field(
        None,
        description='Required. The key of the target resource on which the policies should be resolved.',
    )


class GoogleChromePolicyVersionsV1ResolvedPolicy(BaseModel):
    addedSourceKey: Optional[GoogleChromePolicyVersionsV1PolicyTargetKey] = Field(
        None,
        description='Output only. The added source key establishes at which level an entity was explicitly added for management. This is useful for certain type of policies that are only applied if they are explicitly added for management. For example: apps and networks. An entity can only be deleted from management in an Organizational Unit that it was explicitly added to. If this is not present it means that the policy is managed without the need to explicitly add an entity, for example: standard user or device policies.',
    )
    sourceKey: Optional[GoogleChromePolicyVersionsV1PolicyTargetKey] = Field(
        None,
        description='Output only. The source resource from which this policy value is obtained. May be the same as `targetKey` if the policy is directly modified on the target, otherwise it would be another resource from which the policy gets its value (if applicable). If not present, the source is the default value for the customer.',
    )
    targetKey: Optional[GoogleChromePolicyVersionsV1PolicyTargetKey] = Field(
        None,
        description='Output only. The target resource for which the resolved policy value applies.',
    )
    value: Optional[GoogleChromePolicyVersionsV1PolicyValue] = Field(
        None, description='Output only. The resolved value of the policy.'
    )


class GoogleChromePolicyVersionsV1UpdateGroupPriorityOrderingRequest(BaseModel):
    groupIds: Optional[List[str]] = Field(
        None, description='Required. The group IDs, in desired priority ordering.'
    )
    policyNamespace: Optional[str] = Field(
        None, description='The namespace of the policy type for the request.'
    )
    policySchema: Optional[str] = Field(
        None, description='The schema name of the policy for the request.'
    )
    policyTargetKey: Optional[GoogleChromePolicyVersionsV1PolicyTargetKey] = Field(
        None,
        description='Required. The key of the target for which we want to update the group priority ordering. The target resource must point to an app.',
    )


class GoogleChromePolicyVersionsV1UploadPolicyFileRequest(BaseModel):
    policyField: Optional[str] = Field(
        None,
        description='Required. The fully qualified policy schema and field name this file is uploaded for. This information will be used to validate the content type of the file.',
    )


class GoogleChromePolicyVersionsV1UploadPolicyFileResponse(BaseModel):
    downloadUri: Optional[str] = Field(
        None, description='The uri for end user to download the file.'
    )


class GoogleProtobufEmpty(BaseModel):
    pass


class GoogleTypeDate(BaseModel):
    day: Optional[int] = Field(
        None,
        description="Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.",
    )
    month: Optional[int] = Field(
        None,
        description='Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.',
    )
    year: Optional[int] = Field(
        None,
        description='Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.',
    )


class Proto2EnumValueDescriptorProto(BaseModel):
    name: Optional[str] = None
    number: Optional[int] = None


class Label(Enum):
    LABEL_OPTIONAL = 'LABEL_OPTIONAL'
    LABEL_REQUIRED = 'LABEL_REQUIRED'
    LABEL_REPEATED = 'LABEL_REPEATED'


class Type(Enum):
    TYPE_DOUBLE = 'TYPE_DOUBLE'
    TYPE_FLOAT = 'TYPE_FLOAT'
    TYPE_INT64 = 'TYPE_INT64'
    TYPE_UINT64 = 'TYPE_UINT64'
    TYPE_INT32 = 'TYPE_INT32'
    TYPE_FIXED64 = 'TYPE_FIXED64'
    TYPE_FIXED32 = 'TYPE_FIXED32'
    TYPE_BOOL = 'TYPE_BOOL'
    TYPE_STRING = 'TYPE_STRING'
    TYPE_GROUP = 'TYPE_GROUP'
    TYPE_MESSAGE = 'TYPE_MESSAGE'
    TYPE_BYTES = 'TYPE_BYTES'
    TYPE_UINT32 = 'TYPE_UINT32'
    TYPE_ENUM = 'TYPE_ENUM'
    TYPE_SFIXED32 = 'TYPE_SFIXED32'
    TYPE_SFIXED64 = 'TYPE_SFIXED64'
    TYPE_SINT32 = 'TYPE_SINT32'
    TYPE_SINT64 = 'TYPE_SINT64'


class Proto2FieldDescriptorProto(BaseModel):
    defaultValue: Optional[str] = Field(
        None,
        description='For numeric types, contains the original text representation of the value. For booleans, "true" or "false". For strings, contains the default text contents (not escaped in any way). For bytes, contains the C escaped value. All bytes >= 128 are escaped.',
    )
    jsonName: Optional[str] = Field(
        None,
        description='JSON name of this field. The value is set by protocol compiler. If the user has set a "json_name" option on this field, that option\'s value will be used. Otherwise, it\'s deduced from the field\'s name by converting it to camelCase.',
    )
    label: Optional[Label] = None
    name: Optional[str] = None
    number: Optional[int] = None
    oneofIndex: Optional[int] = Field(
        None,
        description="If set, gives the index of a oneof in the containing type's oneof_decl list. This field is a member of that oneof.",
    )
    proto3Optional: Optional[bool] = Field(
        None,
        description='If true, this is a proto3 "optional". When a proto3 field is optional, it tracks presence regardless of field type. When proto3_optional is true, this field must be belong to a oneof to signal to old proto3 clients that presence is tracked for this field. This oneof is known as a "synthetic" oneof, and this field must be its sole member (each proto3 optional field gets its own synthetic oneof). Synthetic oneofs exist in the descriptor only, and do not generate any API. Synthetic oneofs must be ordered after all "real" oneofs. For message fields, proto3_optional doesn\'t create any semantic change, since non-repeated message fields always track presence. However it still indicates the semantic detail of whether the user wrote "optional" or not. This can be useful for round-tripping the .proto file. For consistency we give message fields a synthetic oneof also, even though it is not required to track presence. This is especially important because the parser can\'t tell if a field is a message or an enum, so it must always create a synthetic oneof. Proto2 optional fields do not set this flag, because they already indicate optional with `LABEL_OPTIONAL`.',
    )
    type: Optional[Type] = Field(
        None,
        description='If type_name is set, this need not be set. If both this and type_name are set, this must be one of TYPE_ENUM, TYPE_MESSAGE or TYPE_GROUP.',
    )
    typeName: Optional[str] = Field(
        None,
        description="For message and enum types, this is the name of the type. If the name starts with a '.', it is fully-qualified. Otherwise, C++-like scoping rules are used to find the type (i.e. first the nested types within this message are searched, then within the parent, on up to the root namespace).",
    )


class Proto2OneofDescriptorProto(BaseModel):
    name: Optional[str] = None


class FieldXgafv(Enum):
    field_1 = '1'
    field_2 = '2'


class Alt(Enum):
    json = 'json'
    media = 'media'
    proto = 'proto'


class ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycle(BaseModel):
    deprecatedInFavorOf: Optional[List[str]] = Field(
        None,
        description='In the event that this policy was deprecated in favor of another policy, the fully qualified namespace(s) of the new policies as they will show in PolicyAPI.',
    )
    description: Optional[str] = Field(
        None, description='Description about current life cycle.'
    )
    endSupport: Optional[GoogleTypeDate] = Field(
        None, description='End supporting date for current policy.'
    )
    policyApiLifecycleStage: Optional[PolicyApiLifecycleStage] = Field(
        None, description='Indicate current life cycle stage of the policy API.'
    )


class GoogleChromePolicyVersionsV1DefineCertificateRequest(BaseModel):
    ceritificateName: Optional[str] = Field(
        None,
        description='Optional. The optional name of the certificate. If not specified, the certificate issuer will be used as the name.',
    )
    certificate: Optional[str] = Field(
        None, description='Required. The raw contents of the .PEM, .CRT, or .CER file.'
    )
    settings: Optional[List[GoogleChromePolicyVersionsV1NetworkSetting]] = Field(
        None,
        description='Optional. Certificate settings within the chrome.networks.certificates namespace.',
    )
    targetResource: Optional[str] = Field(
        None,
        description='Required. The target resource on which this certificate is applied. The following resources are supported: * Organizational Unit ("orgunits/{orgunit_id}")',
    )


class GoogleChromePolicyVersionsV1DefineCertificateResponse(BaseModel):
    networkId: Optional[str] = Field(
        None, description='The guid of the certificate created by the action.'
    )
    settings: Optional[List[GoogleChromePolicyVersionsV1NetworkSetting]] = Field(
        None, description='the affiliated settings of the certificate (NOT IMPLEMENTED)'
    )
    targetResource: Optional[str] = Field(
        None, description='the resource at which the certificate is defined.'
    )


class GoogleChromePolicyVersionsV1DefineNetworkRequest(BaseModel):
    name: Optional[str] = Field(
        None, description='Required. Name of the new created network.'
    )
    settings: Optional[List[GoogleChromePolicyVersionsV1NetworkSetting]] = Field(
        None, description='Required. Detailed network settings.'
    )
    targetResource: Optional[str] = Field(
        None,
        description='Required. The target resource on which this new network will be defined. The following resources are supported: * Organizational Unit ("orgunits/{orgunit_id}")',
    )


class GoogleChromePolicyVersionsV1DefineNetworkResponse(BaseModel):
    networkId: Optional[str] = Field(
        None, description='Network ID of the new created network.'
    )
    settings: Optional[List[GoogleChromePolicyVersionsV1NetworkSetting]] = Field(
        None, description='Detailed network settings of the new created network'
    )
    targetResource: Optional[str] = Field(
        None,
        description='The target resource on which this new network will be defined. The following resources are supported: * Organizational Unit ("orgunits/{orgunit_id}")',
    )


class GoogleChromePolicyVersionsV1DeleteGroupPolicyRequest(BaseModel):
    policySchema: Optional[str] = Field(
        None,
        description='The fully qualified name of the policy schema that is being inherited.',
    )
    policyTargetKey: Optional[GoogleChromePolicyVersionsV1PolicyTargetKey] = Field(
        None,
        description='Required. The key of the target for which we want to modify a policy. The target resource must point to a Group.',
    )


class GoogleChromePolicyVersionsV1FieldConstraints(BaseModel):
    numericRangeConstraint: Optional[
        GoogleChromePolicyVersionsV1NumericRangeConstraint
    ] = Field(None, description='The allowed range for numeric fields.')


class GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequest(BaseModel):
    policySchema: Optional[str] = Field(
        None,
        description='The fully qualified name of the policy schema that is being inherited.',
    )
    policyTargetKey: Optional[GoogleChromePolicyVersionsV1PolicyTargetKey] = Field(
        None,
        description='Required. The key of the target for which we want to modify a policy. The target resource must point to an Org Unit.',
    )


class GoogleChromePolicyVersionsV1ListGroupPriorityOrderingRequest(BaseModel):
    policyNamespace: Optional[str] = Field(
        None, description='The namespace of the policy type for the request.'
    )
    policySchema: Optional[str] = Field(
        None, description='The schema name of the policy for the request.'
    )
    policyTargetKey: Optional[GoogleChromePolicyVersionsV1PolicyTargetKey] = Field(
        None,
        description='Required. The key of the target for which we want to retrieve the group priority ordering. The target resource must point to an app.',
    )


class GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponse(BaseModel):
    groupIds: Optional[List[str]] = Field(
        None, description='Output only. The group IDs, in priority ordering.'
    )
    policyNamespace: Optional[str] = Field(
        None,
        description='Output only. The namespace of the policy type of the group IDs.',
    )
    policySchema: Optional[str] = Field(
        None,
        description='Output only. The schema name of the policy for the group IDs.',
    )
    policyTargetKey: Optional[GoogleChromePolicyVersionsV1PolicyTargetKey] = Field(
        None,
        description='Output only. The target resource for which the group priority ordering has been retrieved.',
    )


class GoogleChromePolicyVersionsV1ModifyGroupPolicyRequest(BaseModel):
    policyTargetKey: Optional[GoogleChromePolicyVersionsV1PolicyTargetKey] = Field(
        None,
        description='Required. The key of the target for which we want to modify a policy. The target resource must point to a Group.',
    )
    policyValue: Optional[GoogleChromePolicyVersionsV1PolicyValue] = Field(
        None, description='The new value for the policy.'
    )
    updateMask: Optional[str] = Field(
        None,
        description="Required. Policy fields to update. Only fields in this mask will be updated; other fields in `policy_value` will be ignored (even if they have values). If a field is in this list it must have a value in 'policy_value'.",
    )


class GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequest(BaseModel):
    policyTargetKey: Optional[GoogleChromePolicyVersionsV1PolicyTargetKey] = Field(
        None,
        description='Required. The key of the target for which we want to modify a policy. The target resource must point to an Org Unit.',
    )
    policyValue: Optional[GoogleChromePolicyVersionsV1PolicyValue] = Field(
        None, description='The new value for the policy.'
    )
    updateMask: Optional[str] = Field(
        None,
        description="Required. Policy fields to update. Only fields in this mask will be updated; other fields in `policy_value` will be ignored (even if they have values). If a field is in this list it must have a value in 'policy_value'.",
    )


class GoogleChromePolicyVersionsV1PolicyModificationError(BaseModel):
    errors: Optional[List[str]] = Field(
        None,
        description='Output only. The non-field errors related to the modification.',
    )
    fieldErrors: Optional[
        List[GoogleChromePolicyVersionsV1PolicyModificationFieldError]
    ] = Field(
        None, description='Output only. The error messages related to the modification.'
    )
    policySchema: Optional[str] = Field(
        None,
        description='Output only. The specific policy schema modification that had an error.',
    )
    policyTargetKey: Optional[GoogleChromePolicyVersionsV1PolicyTargetKey] = Field(
        None,
        description='Output only. The specific policy target modification that had error.',
    )


class GoogleChromePolicyVersionsV1PolicyModificationErrorDetails(BaseModel):
    modificationErrors: Optional[
        List[GoogleChromePolicyVersionsV1PolicyModificationError]
    ] = Field(
        None,
        description='Output only. List of specific policy modifications errors that may have occurred during a modifying request.',
    )


class GoogleChromePolicyVersionsV1PolicySchemaFieldDescription(BaseModel):
    defaultValue: Optional[Any] = Field(
        None, description='Output only. Client default if the policy is unset.'
    )
    description: Optional[str] = Field(
        None,
        description='Deprecated. Use name and field_description instead. The description for the field.',
    )
    field: Optional[str] = Field(
        None,
        description='Output only. The name of the field for associated with this description.',
    )
    fieldConstraints: Optional[GoogleChromePolicyVersionsV1FieldConstraints] = Field(
        None,
        description='Output only. Information on any input constraints associated on the values for the field.',
    )
    fieldDependencies: Optional[
        List[GoogleChromePolicyVersionsV1PolicySchemaFieldDependencies]
    ] = Field(
        None,
        description='Output only. Provides a list of fields and values. At least one of the fields must have the corresponding value in order for this field to be allowed to be set.',
    )
    fieldDescription: Optional[str] = Field(
        None, description='Output only. The description of the field.'
    )
    inputConstraint: Optional[str] = Field(
        None,
        description='Output only. Any input constraints associated on the values for the field.',
    )
    knownValueDescriptions: Optional[
        List[GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescription]
    ] = Field(
        None,
        description='Output only. If the field has a set of known values, this field will provide a description for these values.',
    )
    name: Optional[str] = Field(None, description='Output only. The name of the field.')
    nestedFieldDescriptions: Optional[
        List[GoogleChromePolicyVersionsV1PolicySchemaFieldDescription]
    ] = Field(
        None,
        description='Output only. Provides the description of the fields nested in this field, if the field is a message type that defines multiple fields.',
    )
    requiredItems: Optional[
        List[GoogleChromePolicyVersionsV1PolicySchemaRequiredItems]
    ] = Field(
        None,
        description='Output only. Provides a list of fields that are required to be set if this field has a certain value.',
    )


class GoogleChromePolicyVersionsV1ResolveResponse(BaseModel):
    nextPageToken: Optional[str] = Field(
        None,
        description='The page token used to get the next set of resolved policies found by the request.',
    )
    resolvedPolicies: Optional[List[GoogleChromePolicyVersionsV1ResolvedPolicy]] = (
        Field(
            None,
            description='The list of resolved policies found by the resolve request.',
        )
    )


class Proto2EnumDescriptorProto(BaseModel):
    name: Optional[str] = None
    value: Optional[List[Proto2EnumValueDescriptorProto]] = None


class GoogleChromePolicyVersionsV1BatchDeleteGroupPoliciesRequest(BaseModel):
    requests: Optional[List[GoogleChromePolicyVersionsV1DeleteGroupPolicyRequest]] = (
        Field(
            None,
            description='List of policies that will be deleted as defined by the `requests`. All requests in the list must follow these restrictions: 1. All schemas in the list must have the same root namespace. 2. All `policyTargetKey.targetResource` values must point to a group resource. 3. All `policyTargetKey` values must have the same `app_id` key name in the `additionalTargetKeys`. 4. No two modification requests can reference the same `policySchema` + ` policyTargetKey` pair. ',
        )
    )


class GoogleChromePolicyVersionsV1BatchInheritOrgUnitPoliciesRequest(BaseModel):
    requests: Optional[
        List[GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequest]
    ] = Field(
        None,
        description='List of policies that have to inherit their values as defined by the `requests`. All requests in the list must follow these restrictions: 1. All schemas in the list must have the same root namespace. 2. All `policyTargetKey.targetResource` values must point to an org unit resource. 3. All `policyTargetKey` values must have the same key names in the ` additionalTargetKeys`. This also means if one of the targets has an empty `additionalTargetKeys` map, all of the targets must have an empty `additionalTargetKeys` map. 4. No two modification requests can reference the same `policySchema` + ` policyTargetKey` pair. ',
    )


class GoogleChromePolicyVersionsV1BatchModifyGroupPoliciesRequest(BaseModel):
    requests: Optional[List[GoogleChromePolicyVersionsV1ModifyGroupPolicyRequest]] = (
        Field(
            None,
            description='List of policies to modify as defined by the `requests`. All requests in the list must follow these restrictions: 1. All schemas in the list must have the same root namespace. 2. All `policyTargetKey.targetResource` values must point to a group resource. 3. All `policyTargetKey` values must have the same `app_id` key name in the `additionalTargetKeys`. 4. No two modification requests can reference the same `policySchema` + ` policyTargetKey` pair. ',
        )
    )


class GoogleChromePolicyVersionsV1BatchModifyOrgUnitPoliciesRequest(BaseModel):
    requests: Optional[List[GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequest]] = (
        Field(
            None,
            description='List of policies to modify as defined by the `requests`. All requests in the list must follow these restrictions: 1. All schemas in the list must have the same root namespace. 2. All `policyTargetKey.targetResource` values must point to an org unit resource. 3. All `policyTargetKey` values must have the same key names in the ` additionalTargetKeys`. This also means if one of the targets has an empty `additionalTargetKeys` map, all of the targets must have an empty `additionalTargetKeys` map. 4. No two modification requests can reference the same `policySchema` + ` policyTargetKey` pair. ',
        )
    )


class Proto2DescriptorProto(BaseModel):
    enumType: Optional[List[Proto2EnumDescriptorProto]] = None
    field: Optional[List[Proto2FieldDescriptorProto]] = None
    name: Optional[str] = None
    nestedType: Optional[List[Proto2DescriptorProto]] = None
    oneofDecl: Optional[List[Proto2OneofDescriptorProto]] = None


class Proto2FileDescriptorProto(BaseModel):
    enumType: Optional[List[Proto2EnumDescriptorProto]] = None
    messageType: Optional[List[Proto2DescriptorProto]] = Field(
        None, description='All top-level definitions in this file.'
    )
    name: Optional[str] = Field(
        None, description='file name, relative to root of source tree'
    )
    package: Optional[str] = Field(None, description='e.g. "foo", "foo.bar", etc.')
    syntax: Optional[str] = Field(
        None,
        description='The syntax of the proto file. The supported values are "proto2", "proto3", and "editions". If `edition` is present, this value must be "editions".',
    )


class GoogleChromePolicyVersionsV1PolicySchema(BaseModel):
    accessRestrictions: Optional[List[str]] = Field(
        None,
        description='Output only. Specific access restrictions related to this policy.',
    )
    additionalTargetKeyNames: Optional[
        List[GoogleChromePolicyVersionsV1AdditionalTargetKeyName]
    ] = Field(
        None,
        description='Output only. Additional key names that will be used to identify the target of the policy value. When specifying a `policyTargetKey`, each of the additional keys specified here will have to be included in the `additionalTargetKeys` map.',
    )
    categoryTitle: Optional[str] = Field(
        None, description='Title of the category in which a setting belongs.'
    )
    definition: Optional[Proto2FileDescriptorProto] = Field(
        None, description='Schema definition using proto descriptor.'
    )
    fieldDescriptions: Optional[
        List[GoogleChromePolicyVersionsV1PolicySchemaFieldDescription]
    ] = Field(
        None,
        description='Output only. Detailed description of each field that is part of the schema.',
    )
    name: Optional[str] = Field(
        None,
        description='Format: name=customers/{customer}/policySchemas/{schema_namespace}',
    )
    notices: Optional[
        List[GoogleChromePolicyVersionsV1PolicySchemaNoticeDescription]
    ] = Field(
        None,
        description='Output only. Special notice messages related to setting certain values in certain fields in the schema.',
    )
    policyApiLifecycle: Optional[
        ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycle
    ] = Field(None, description='Output only. Current lifecycle information.')
    policyDescription: Optional[str] = Field(
        None,
        description='Output only. Description about the policy schema for user consumption.',
    )
    schemaName: Optional[str] = Field(
        None,
        description='Output only. The fully qualified name of the policy schema. This value is used to fill the field `policy_schema` in PolicyValue when calling BatchInheritOrgUnitPolicies BatchModifyOrgUnitPolicies BatchModifyGroupPolicies or BatchDeleteGroupPolicies.',
    )
    supportUri: Optional[str] = Field(
        None, description='Output only. URI to related support article for this schema.'
    )
    validTargetResources: Optional[List[ValidTargetResource]] = Field(
        None,
        description='Output only. Information about applicable target resources for the policy.',
    )


class GoogleChromePolicyVersionsV1ListPolicySchemasResponse(BaseModel):
    nextPageToken: Optional[str] = Field(
        None, description='The page token used to get the next page of policy schemas.'
    )
    policySchemas: Optional[List[GoogleChromePolicyVersionsV1PolicySchema]] = Field(
        None, description='The list of policy schemas that match the query.'
    )


GoogleChromePolicyVersionsV1PolicySchemaFieldDescription.model_rebuild()
Proto2DescriptorProto.model_rebuild()
