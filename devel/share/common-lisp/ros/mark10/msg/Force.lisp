; Auto-generated. Do not edit!


(cl:in-package mark10-msg)


;//! \htmlinclude Force.msg.html

(cl:defclass <Force> (roslisp-msg-protocol:ros-message)
  ((force
    :reader force
    :initarg :force
    :type cl:float
    :initform 0.0)
   (unit
    :reader unit
    :initarg :unit
    :type cl:string
    :initform ""))
)

(cl:defclass Force (<Force>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Force>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Force)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mark10-msg:<Force> is deprecated: use mark10-msg:Force instead.")))

(cl:ensure-generic-function 'force-val :lambda-list '(m))
(cl:defmethod force-val ((m <Force>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mark10-msg:force-val is deprecated.  Use mark10-msg:force instead.")
  (force m))

(cl:ensure-generic-function 'unit-val :lambda-list '(m))
(cl:defmethod unit-val ((m <Force>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mark10-msg:unit-val is deprecated.  Use mark10-msg:unit instead.")
  (unit m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Force>) ostream)
  "Serializes a message object of type '<Force>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'force))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'unit))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'unit))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Force>) istream)
  "Deserializes a message object of type '<Force>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'force) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'unit) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'unit) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Force>)))
  "Returns string type for a message object of type '<Force>"
  "mark10/Force")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Force)))
  "Returns string type for a message object of type 'Force"
  "mark10/Force")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Force>)))
  "Returns md5sum for a message object of type '<Force>"
  "ef3c99a919c971d6e0f206376229102e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Force)))
  "Returns md5sum for a message object of type 'Force"
  "ef3c99a919c971d6e0f206376229102e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Force>)))
  "Returns full string definition for message of type '<Force>"
  (cl:format cl:nil "float32 force~%string unit~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Force)))
  "Returns full string definition for message of type 'Force"
  (cl:format cl:nil "float32 force~%string unit~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Force>))
  (cl:+ 0
     4
     4 (cl:length (cl:slot-value msg 'unit))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Force>))
  "Converts a ROS message object to a list"
  (cl:list 'Force
    (cl:cons ':force (force msg))
    (cl:cons ':unit (unit msg))
))
