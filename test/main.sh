#!/usr/bin/env bash
DEBUG=1

DIR="$(cd "$( dirname "${0}" )" && pwd)"
[[ -z "${ANSIBLE_CONFIG}" ]] && export ANSIBLE_CONFIG="${DIR}/ansible.cfg"
[[ -z "${ANSIBLE_INVENTORY}" ]] && export ANSIBLE_INVENTORY="${DIR}/vars"
[[ -z "${ANSIBLE_ROLES_PATH}" ]] && export ANSIBLE_ROLES_PATH="${DIR}/roles"
[[ -z "${ANSIBLE_VARS_PLUGINS}" ]] && export ANSIBLE_VARS_PLUGINS="${DIR}/.."

[[ "${DEBUG}" != "1" ]] || echo
[[ "${DEBUG}" != "1" ]] || echo Running from directory: "${DIR}"
[[ "${DEBUG}" != "1" ]] || echo Using ansible configuration: "${ANSIBLE_CONFIG}"
[[ "${DEBUG}" != "1" ]] || echo Using inventory directory: "${ANSIBLE_INVENTORY}"
[[ "${DEBUG}" != "1" ]] || echo Using roles path: "${ANSIBLE_ROLES_PATH}"
[[ "${DEBUG}" != "1" ]] || echo Using vars plugins directory:"${ANSIBLE_VARS_PLUGINS}"
[[ "${DEBUG}" != "1" ]] || echo

[[ "${DEBUG}" != "1" ]] || verbose=-vv

time ansible-playbook ${verbose} "${DIR}/main.yml"
exit $?

