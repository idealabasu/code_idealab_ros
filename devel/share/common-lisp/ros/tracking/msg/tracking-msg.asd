
(cl:in-package :asdf)

(defsystem "tracking-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "marker" :depends-on ("_package_marker"))
    (:file "_package_marker" :depends-on ("_package"))
  ))