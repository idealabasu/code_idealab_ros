; Auto-generated. Do not edit!


(cl:in-package tracking-msg)


;//! \htmlinclude marker.msg.html

(cl:defclass <marker> (roslisp-msg-protocol:ros-message)
  ((color
    :reader color
    :initarg :color
    :type cl:string
    :initform "")
   (x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0))
)

(cl:defclass marker (<marker>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <marker>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'marker)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tracking-msg:<marker> is deprecated: use tracking-msg:marker instead.")))

(cl:ensure-generic-function 'color-val :lambda-list '(m))
(cl:defmethod color-val ((m <marker>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tracking-msg:color-val is deprecated.  Use tracking-msg:color instead.")
  (color m))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <marker>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tracking-msg:x-val is deprecated.  Use tracking-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <marker>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tracking-msg:y-val is deprecated.  Use tracking-msg:y instead.")
  (y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <marker>) ostream)
  "Serializes a message object of type '<marker>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'color))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'color))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <marker>) istream)
  "Deserializes a message object of type '<marker>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'color) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'color) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<marker>)))
  "Returns string type for a message object of type '<marker>"
  "tracking/marker")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'marker)))
  "Returns string type for a message object of type 'marker"
  "tracking/marker")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<marker>)))
  "Returns md5sum for a message object of type '<marker>"
  "9eab6da5b2968819e8b305355e8d814c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'marker)))
  "Returns md5sum for a message object of type 'marker"
  "9eab6da5b2968819e8b305355e8d814c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<marker>)))
  "Returns full string definition for message of type '<marker>"
  (cl:format cl:nil "string color~%float32 x~%float32 y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'marker)))
  "Returns full string definition for message of type 'marker"
  (cl:format cl:nil "string color~%float32 x~%float32 y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <marker>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'color))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <marker>))
  "Converts a ROS message object to a list"
  (cl:list 'marker
    (cl:cons ':color (color msg))
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
))
