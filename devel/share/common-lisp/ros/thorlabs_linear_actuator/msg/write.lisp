; Auto-generated. Do not edit!


(cl:in-package thorlabs_linear_actuator-msg)


;//! \htmlinclude write.msg.html

(cl:defclass <write> (roslisp-msg-protocol:ros-message)
  ((register
    :reader register
    :initarg :register
    :type cl:fixnum
    :initform 0)
   (value
    :reader value
    :initarg :value
    :type cl:fixnum
    :initform 0))
)

(cl:defclass write (<write>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <write>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'write)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name thorlabs_linear_actuator-msg:<write> is deprecated: use thorlabs_linear_actuator-msg:write instead.")))

(cl:ensure-generic-function 'register-val :lambda-list '(m))
(cl:defmethod register-val ((m <write>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader thorlabs_linear_actuator-msg:register-val is deprecated.  Use thorlabs_linear_actuator-msg:register instead.")
  (register m))

(cl:ensure-generic-function 'value-val :lambda-list '(m))
(cl:defmethod value-val ((m <write>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader thorlabs_linear_actuator-msg:value-val is deprecated.  Use thorlabs_linear_actuator-msg:value instead.")
  (value m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <write>) ostream)
  "Serializes a message object of type '<write>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'register)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'value)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <write>) istream)
  "Deserializes a message object of type '<write>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'register)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'value)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<write>)))
  "Returns string type for a message object of type '<write>"
  "thorlabs_linear_actuator/write")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'write)))
  "Returns string type for a message object of type 'write"
  "thorlabs_linear_actuator/write")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<write>)))
  "Returns md5sum for a message object of type '<write>"
  "42a1ebb3a1d2bdfda4b28ad577afa942")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'write)))
  "Returns md5sum for a message object of type 'write"
  "42a1ebb3a1d2bdfda4b28ad577afa942")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<write>)))
  "Returns full string definition for message of type '<write>"
  (cl:format cl:nil "uint8 register~%uint8 value~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'write)))
  "Returns full string definition for message of type 'write"
  (cl:format cl:nil "uint8 register~%uint8 value~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <write>))
  (cl:+ 0
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <write>))
  "Converts a ROS message object to a list"
  (cl:list 'write
    (cl:cons ':register (register msg))
    (cl:cons ':value (value msg))
))
