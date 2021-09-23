; Auto-generated. Do not edit!


(cl:in-package universal_robots-msg)


;//! \htmlinclude position_command.msg.html

(cl:defclass <position_command> (roslisp-msg-protocol:ros-message)
  ((p
    :reader p
    :initarg :p
    :type (cl:vector cl:float)
   :initform (cl:make-array 3 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass position_command (<position_command>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <position_command>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'position_command)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name universal_robots-msg:<position_command> is deprecated: use universal_robots-msg:position_command instead.")))

(cl:ensure-generic-function 'p-val :lambda-list '(m))
(cl:defmethod p-val ((m <position_command>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader universal_robots-msg:p-val is deprecated.  Use universal_robots-msg:p instead.")
  (p m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <position_command>) ostream)
  "Serializes a message object of type '<position_command>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'p))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <position_command>) istream)
  "Deserializes a message object of type '<position_command>"
  (cl:setf (cl:slot-value msg 'p) (cl:make-array 3))
  (cl:let ((vals (cl:slot-value msg 'p)))
    (cl:dotimes (i 3)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<position_command>)))
  "Returns string type for a message object of type '<position_command>"
  "universal_robots/position_command")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'position_command)))
  "Returns string type for a message object of type 'position_command"
  "universal_robots/position_command")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<position_command>)))
  "Returns md5sum for a message object of type '<position_command>"
  "1abbaca176899a0863a2922ff57df9ac")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'position_command)))
  "Returns md5sum for a message object of type 'position_command"
  "1abbaca176899a0863a2922ff57df9ac")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<position_command>)))
  "Returns full string definition for message of type '<position_command>"
  (cl:format cl:nil "float64[3] p~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'position_command)))
  "Returns full string definition for message of type 'position_command"
  (cl:format cl:nil "float64[3] p~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <position_command>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'p) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <position_command>))
  "Converts a ROS message object to a list"
  (cl:list 'position_command
    (cl:cons ':p (p msg))
))
