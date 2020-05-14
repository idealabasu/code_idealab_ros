
(cl:in-package :asdf)

(defsystem "mark10-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Force" :depends-on ("_package_Force"))
    (:file "_package_Force" :depends-on ("_package"))
  ))