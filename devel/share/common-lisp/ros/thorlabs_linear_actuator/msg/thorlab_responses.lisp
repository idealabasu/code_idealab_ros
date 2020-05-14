; Auto-generated. Do not edit!


(cl:in-package thorlabs_linear_actuator-msg)


;//! \htmlinclude thorlab_responses.msg.html

(cl:defclass <thorlab_responses> (roslisp-msg-protocol:ros-message)
  ((response
    :reader response
    :initarg :response
    :type cl:string
    :initform ""))
)

(cl:defclass thorlab_responses (<thorlab_responses>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <thorlab_responses>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'thorlab_responses)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name thorlabs_linear_actuator-msg:<thorlab_responses> is deprecated: use thorlabs_linear_actuator-msg:thorlab_responses instead.")))

(cl:ensure-generic-function 'response-val :lambda-list '(m))
(cl:defmethod response-val ((m <thorlab_responses>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader thorlabs_linear_actuator-msg:response-val is deprecated.  Use thorlabs_linear_actuator-msg:response instead.")
  (response m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <thorlab_responses>) ostream)
  "Serializes a message object of type '<thorlab_responses>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'response))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'response))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <thorlab_responses>) istream)
  "Deserializes a message object of type '<thorlab_responses>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'response) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'response) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<thorlab_responses>)))
  "Returns string type for a message object of type '<thorlab_responses>"
  "thorlabs_linear_actuator/thorlab_responses")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'thorlab_responses)))
  "Returns string type for a message object of type 'thorlab_responses"
  "thorlabs_linear_actuator/thorlab_responses")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<thorlab_responses>)))
  "Returns md5sum for a message object of type '<thorlab_responses>"
  "6de314e2dc76fbff2b6244a6ad70b68d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'thorlab_responses)))
  "Returns md5sum for a message object of type 'thorlab_responses"
  "6de314e2dc76fbff2b6244a6ad70b68d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<thorlab_responses>)))
  "Returns full string definition for message of type '<thorlab_responses>"
  (cl:format cl:nil "string response~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'thorlab_responses)))
  "Returns full string definition for message of type 'thorlab_responses"
  (cl:format cl:nil "string response~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <thorlab_responses>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'response))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <thorlab_responses>))
  "Converts a ROS message object to a list"
  (cl:list 'thorlab_responses
    (cl:cons ':response (response msg))
))
