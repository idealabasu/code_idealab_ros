; Auto-generated. Do not edit!


(cl:in-package ati_nano-msg)


;//! \htmlinclude write.msg.html

(cl:defclass <write> (roslisp-msg-protocol:ros-message)
  ((fx
    :reader fx
    :initarg :fx
    :type cl:float
    :initform 0.0)
   (fy
    :reader fy
    :initarg :fy
    :type cl:float
    :initform 0.0)
   (fz
    :reader fz
    :initarg :fz
    :type cl:float
    :initform 0.0)
   (tx
    :reader tx
    :initarg :tx
    :type cl:float
    :initform 0.0)
   (ty
    :reader ty
    :initarg :ty
    :type cl:float
    :initform 0.0)
   (tz
    :reader tz
    :initarg :tz
    :type cl:float
    :initform 0.0))
)

(cl:defclass write (<write>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <write>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'write)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ati_nano-msg:<write> is deprecated: use ati_nano-msg:write instead.")))

(cl:ensure-generic-function 'fx-val :lambda-list '(m))
(cl:defmethod fx-val ((m <write>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ati_nano-msg:fx-val is deprecated.  Use ati_nano-msg:fx instead.")
  (fx m))

(cl:ensure-generic-function 'fy-val :lambda-list '(m))
(cl:defmethod fy-val ((m <write>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ati_nano-msg:fy-val is deprecated.  Use ati_nano-msg:fy instead.")
  (fy m))

(cl:ensure-generic-function 'fz-val :lambda-list '(m))
(cl:defmethod fz-val ((m <write>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ati_nano-msg:fz-val is deprecated.  Use ati_nano-msg:fz instead.")
  (fz m))

(cl:ensure-generic-function 'tx-val :lambda-list '(m))
(cl:defmethod tx-val ((m <write>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ati_nano-msg:tx-val is deprecated.  Use ati_nano-msg:tx instead.")
  (tx m))

(cl:ensure-generic-function 'ty-val :lambda-list '(m))
(cl:defmethod ty-val ((m <write>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ati_nano-msg:ty-val is deprecated.  Use ati_nano-msg:ty instead.")
  (ty m))

(cl:ensure-generic-function 'tz-val :lambda-list '(m))
(cl:defmethod tz-val ((m <write>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ati_nano-msg:tz-val is deprecated.  Use ati_nano-msg:tz instead.")
  (tz m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <write>) ostream)
  "Serializes a message object of type '<write>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'fx))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'fy))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'fz))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'tx))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'ty))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'tz))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <write>) istream)
  "Deserializes a message object of type '<write>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'fx) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'fy) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'fz) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'tx) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'ty) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'tz) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<write>)))
  "Returns string type for a message object of type '<write>"
  "ati_nano/write")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'write)))
  "Returns string type for a message object of type 'write"
  "ati_nano/write")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<write>)))
  "Returns md5sum for a message object of type '<write>"
  "525bd7f46f455baf22b587d94f926977")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'write)))
  "Returns md5sum for a message object of type 'write"
  "525bd7f46f455baf22b587d94f926977")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<write>)))
  "Returns full string definition for message of type '<write>"
  (cl:format cl:nil "float32 fx~%float32 fy~%float32 fz~%float32 tx~%float32 ty~%float32 tz~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'write)))
  "Returns full string definition for message of type 'write"
  (cl:format cl:nil "float32 fx~%float32 fy~%float32 fz~%float32 tx~%float32 ty~%float32 tz~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <write>))
  (cl:+ 0
     4
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <write>))
  "Converts a ROS message object to a list"
  (cl:list 'write
    (cl:cons ':fx (fx msg))
    (cl:cons ':fy (fy msg))
    (cl:cons ':fz (fz msg))
    (cl:cons ':tx (tx msg))
    (cl:cons ':ty (ty msg))
    (cl:cons ':tz (tz msg))
))
